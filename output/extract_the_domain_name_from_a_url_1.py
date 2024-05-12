"""Kata - Extract the domain name from a URL

completed at: 2022-09-10 19:54:53
by: Jakub Červinka

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
```
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
```
"""

def domain_name(url):
    import urllib.parse
    if not url.startswith('http'):
        url = 'http://' + url
    split_result = urllib.parse.urlsplit(url)
    parts = split_result.netloc.split('.')
    return parts[1] if parts[0] == 'www' else parts[0]

