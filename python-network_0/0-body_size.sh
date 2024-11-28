#!/bin/bash
# Bash script that takes a URL, sends the request, and displays the size of the response body.
curl -s -w '%{size_download}\n' -o /dev/null "$1"
