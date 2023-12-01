#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value"""

import urllib.request
import sys
if len(sys.argv) != 2:
    print("{} <URl>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
