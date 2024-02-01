#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2:
        data = {'q': sys.argv[1]}
    elif sys.argv[1] is None:
        data = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        res = r.json()
        id, name = res.get('id'), res.get('name')
        if len(res) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")
