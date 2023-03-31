#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""


import sys
import requests


if __name__ == "__main__":
    repo, owner = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner, repo)

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
