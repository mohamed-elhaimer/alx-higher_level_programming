#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        res = response.read()
        print("Your email is: ".format(res.decode('utf-8')))
