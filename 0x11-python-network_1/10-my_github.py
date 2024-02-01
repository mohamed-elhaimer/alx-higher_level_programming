#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(url, basic)
    print(req.json().get('id'))
