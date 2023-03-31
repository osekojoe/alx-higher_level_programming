#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the
 response (decoded in utf-8)
 manage urllib.error.HTTPError exceptions and print: Error code: followed
 by the HTTP status code
 Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""


import sys
from urllib.request import Request, urlopen
from urllib.error import URLError


if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
        response = response.read().decode('ascii')
        print(response)
    except URLError as e:
        if hasattr(e, 'code'):
            print('Error code: ', e.code)
    else:
        pass
