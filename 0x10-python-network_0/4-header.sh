#!/bin/bash
# Use curl to send a GET request with a custom header and display the body
curl -s -H "X-School_User_id: 98" "$1"
