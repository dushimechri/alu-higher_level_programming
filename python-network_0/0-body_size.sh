#!/bin/bash
#Bash script that takes & send the URL and display size.
curl -s "$1" | wc -c
