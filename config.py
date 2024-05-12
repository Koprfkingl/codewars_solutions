import logging
import logging.config
import os
from pathlib import Path

from dotenv import dotenv_values

ENV = {
    **dotenv_values('.env_secret'),  # secret values
    **dotenv_values('.env_public'),
    **os.environ,  # override loaded values with environment variables
}

CURRENT_DIR = Path.cwd()
LOGS_DIR = CURRENT_DIR / 'logs'
OUTPUT_DIR = CURRENT_DIR / 'output'

# kata
KATA_TEMPLATE_STR = """\
\"\"\"Kata - {name}

completed at: {completed_at:%Y-%m-%d %H:%M:%S}
by: {completed_by}

{description}
\"\"\"

{code}
"""

LOG_CONF = {
    'version': 1,
    'formatters': {
        'file_form': {
            'format': '%(asctime)s - %(levelname)-8s - %(funcName)-22s - %(message)s'
        },
        'console_form': {
            'format': '%(levelname)-8s - %(message)s'
        },
    },
    'handlers': {
        'console_hand': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'level': 'INFO',
            'formatter': 'console_form',
        },
        'file_hand_rot': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGS_DIR / 'codewars_backup.log',
            'maxBytes': 3_145_728,  # 3MB
            'backupCount': 5,  # five files with log backup
            'level': 'DEBUG',
            'encoding': 'utf-8',
            'formatter': 'file_form',
        },
    },
    'loggers': {
        'cw_logger': {
            'handlers': ['console_hand', 'file_hand_rot'],
            'level': 'DEBUG',
        }
    }
}


def setup_logging():
    p = CURRENT_DIR / 'logs'
    p.mkdir(parents=True, exist_ok=True)
    logging.config.dictConfig(LOG_CONF)
    log = logging.getLogger(__name__)
    log.debug('Logging was set up.')
