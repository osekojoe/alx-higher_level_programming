#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the
  GitHub API to display your id

  Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""


import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username, password = sys.argv[1], sys.argv[2]
    url = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, password)
    r = requests.get(url, auth=auth)
    print(r.json().get('id'))
