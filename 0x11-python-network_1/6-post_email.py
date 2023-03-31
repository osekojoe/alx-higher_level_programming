#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
The email must be sent in the variable email

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}

    res = requests.post(url, data=payload)
    print(res.text)
