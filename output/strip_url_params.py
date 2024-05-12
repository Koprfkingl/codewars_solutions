"""Kata - Strip Url Params

completed at: 2023-05-22 20:47:21
by: Jakub Červinka

#### Complete the method so that it does the following:

- Removes any duplicate query string parameters from the url (the first occurence should be kept)
- Removes any query string parameters specified within the 2nd argument (optional array)


#### Examples:

```javascript
stripUrlParams('www.codewars.com?a=1&b=2&a=2') === 'www.codewars.com?a=1&b=2'
stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) === 'www.codewars.com?a=1'
stripUrlParams('www.codewars.com', ['b']) === 'www.codewars.com'
```
```ruby
strip_url_params('www.codewars.com?a=1&b=2&a=2') == 'www.codewars.com?a=1&b=2'
strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) == 'www.codewars.com?a=1'
strip_url_params('www.codewars.com', ['b']) == 'www.codewars.com'
```
```python
strip_url_params('www.codewars.com?a=1&b=2&a=2') == 'www.codewars.com?a=1&b=2'
strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) == 'www.codewars.com?a=1'
strip_url_params('www.codewars.com', ['b']) == 'www.codewars.com'
```
"""

from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
from urllib.parse import urlunparse

def strip_url_params(url, params_to_strip=None):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    params_to_strip = params_to_strip or set()
    
    query_params = {
        k: v[0]
        for k, v in query_params.items()
        if k not in params_to_strip
    }

    new_query_string = urlencode(query_params, doseq=True)
    new_url_parts = parsed_url._replace(query=new_query_string)
    stripped_url = urlunparse(new_url_parts)

    return stripped_url

