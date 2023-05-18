import datetime
import itertools
import json
import logging
import re
import textwrap
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from http.cookies import SimpleCookie
from pathlib import Path
from typing import TypeVar

import requests
from requests import Response
from requests_html import HTMLSession
from tqdm import tqdm

import config
from config import ENV
from config import USER_URL
from config import setup_logging

Kata = TypeVar('Kata')

setup_logging()

log = logging.getLogger('cw_logger')


@dataclass
class Kata:
    id: str
    name: str
    slug: str
    completedLanguages: list[str]
    completedAt: str
    code: str = ''
    description: str = ''
    uploaded: bool = False

    def __post_init__(self):
        # parse
        self.completed_at = datetime.datetime.fromisoformat(self.completedAt[:-5])
        self.completed_languages = self.completedLanguages
        # remove the non pythonic names
        del self.completedAt
        del self.completedLanguages

    def to_file(self):
        log.debug(f'saving kata {self.slug} to file')
        f_name = self.slug.replace('-', '_') + '.py'
        with open(config.OUTPUT_DIR / f_name, 'w', encoding='utf-8') as f:
            f.write(self.templated_str)

    @property
    def templated_str(self) -> str:
        return config.KATA_TEMPLATE_STR.format(**self.__dict__)

    def __str__(self):
        return f'Kata: {self.name}'

    __repr__ = __str__


class CodewarsAgent:

    def __init__(self):
        self.session = HTMLSession()
        cookies = self._parse_cookie_env(ENV['CW_COOKIE'])
        self.session.cookies = cookies
        self.completed_katas = []
        self.uploaded_katas = set()
        self.backup_file_name = 'uploaded_katas.txt'
        log.debug('Codewars agent prepared')

    @staticmethod
    def _parse_cookie_env(raw_cookie: str) -> dict:
        log.debug('parsing cookies')
        cookie = SimpleCookie()
        cookie.load(raw_cookie)
        return requests.utils.cookiejar_from_dict({
            key: morsel.value
            for key, morsel in cookie.items()
        })

    def get_user_data(self, url: str) -> dict:
        """Fetch user info json from public API."""
        log.debug('getting user data')
        r = self.session.get(url)
        return r.json()

    @staticmethod
    def parse_user_info(user_data: dict) -> str:
        """Parse the provided user info into a readable paragraph."""
        return textwrap.dedent(
            f"""Hi {user_data['name']},
           you are currently at {user_data['ranks']['overall']['name']} 
           with {user_data['codeChallenges']['totalCompleted']} completed katas."""
        )

    def load_completed_katas_data(self):
        """Fetch all completed katas info jsons.

        Save it internally for later use.
        """

        log.debug('loading katas data')
        url = fr"{USER_URL}/code-challenges/completed"

        self.completed_katas = []

        for page_num in itertools.count():
            log.debug(f'\tloading page {page_num}')
            resp_json = self.session.get(url, params={'page': page_num}).json()
            self.completed_katas.extend(resp_json['data'])

            if page_num == resp_json['totalPages'] - 1:
                log.debug(f'loaded {len(self.completed_katas)} katas')
                break

    def load_uploaded_katas(self):
        file = Path(self.backup_file_name)
        file.touch(exist_ok=True)
        with open(file) as f:
            self.uploaded_katas = set(f.read().splitlines())

    def update_uploaded_katas(self):
        file = Path(self.backup_file_name)
        with open(file, 'a') as f:
            f.writelines('\n'.join(
                k['slug'] for k in self.katas_to_download
            ))

    def get_kata_data(self, kata_id: str) -> tuple[str, str]:
        """Get description and code for given kata_id."""

        url = fr'https://www.codewars.com/kata/{kata_id}/solutions/python'
        params = {'filter': 'me', 'sort': 'best_practice', 'invalids': 'false'}
        r = self.session.get(url=url, params=params)
        description, code = self._parse_response(r)
        return description, code

    @property
    def katas_to_download(self):
        pred = lambda k: k['slug'] not in self.uploaded_katas
        return list(filter(pred, self.completed_katas))

    @staticmethod
    def _parse_response(response: Response) -> tuple[str, str]:
        log.debug('parsing kata description and solution')
        element = response.html.find('script')[-2]
        text = re.findall(r'JSON\.parse\((.*)\),', element.full_text)[0]
        script_data = json.loads(json.loads(text))  # double decode
        return script_data['description'], script_data['solution']

    def create_kata_obj(self, kata_data: dict) -> Kata:
        kata = Kata(**kata_data)
        kata.description, kata.code = self.get_kata_data(kata.id)
        return kata

    def thread_target(self, kata_data):
        kata = self.create_kata_obj(kata_data)
        kata.to_file()


if __name__ == '__main__':
    log.info(' START '.center(80, '='))

    log.debug('preparing output folder')
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # prepare online agent
    cw = CodewarsAgent()

    user_data = cw.get_user_data(USER_URL)
    log.info(cw.parse_user_info(user_data))

    # load completed katas info from public api
    cw.load_completed_katas_data()

    cw.load_uploaded_katas()

    log.info('downloading katas')
    # run the threads
    with ThreadPoolExecutor(max_workers=30) as executor:
        list(tqdm(
            executor.map(
                cw.thread_target,
                cw.katas_to_download
            ),
            total=len(cw.katas_to_download)
        ))
    log.info('download finished')

    cw.update_uploaded_katas()
