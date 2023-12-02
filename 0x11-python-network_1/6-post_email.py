#!/usr/bin/python3
"""Sends a POST request with an email parameter"""
import requests
import sys

if len(sys.argv) != 3:
    print("{} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]
data = {'email': email}
response - requests.post(url, data=data)
print(response.text)
