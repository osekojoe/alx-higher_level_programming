#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the
 response (decoded in utf-8)
 manage urllib.error.HTTPError exceptions and print: Error code: followed
 by the HTTP status code
 Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""


import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
