#!/usr/bin/python3
"""Displays the body of the response and handles HTTPError"""

import sys
import urllib.request

if len(sys.argv) != 2:
    print("{} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
