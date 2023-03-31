#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
Usage: ./0-hbtn_status.py | cat -e
"""


import urllib.request


if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('UTF8')))
