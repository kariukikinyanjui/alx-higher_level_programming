#!/usr/bin/python3
"""Sends a POST  request with an email parameter"""
import sys
import urllib.request

url = sys.argv[1]
email = sys.argv[2]
data = 'email={}'.format(email).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    body = response.read().decode('utf-8')
    print(body)
