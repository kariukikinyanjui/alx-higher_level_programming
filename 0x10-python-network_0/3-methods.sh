#!/bin/bash
# Use curl to send an OPTIONS request to the URL and display allowed methods
curl -s -i -X OPTIONS "$1" | awk -F': ' '/Allow/{print $2}'
