#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print("{}".format(response.headers.get("X-Request-Id")))
