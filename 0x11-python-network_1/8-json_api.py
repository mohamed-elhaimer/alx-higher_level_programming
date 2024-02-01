#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    data = {'q': sys.argv[1]}
    if data['q'] is None:
        data['q'] = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        res = r.json()
        if len(res) == 0 and 'id' not in res and 'name' not in res:
            print("No result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
    except ValueError:
        print("Not a valid JSON")
