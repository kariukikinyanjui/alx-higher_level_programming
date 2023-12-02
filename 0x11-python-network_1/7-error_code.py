#!/usr/bin/python3
"""Displays the body of the response and handles HTTP errors"""
import sys
import requests

if len(sys.argv) != 2:
    print("{} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    print(response.text)
