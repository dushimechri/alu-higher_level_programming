#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    # Send GET request
    r = requests.get("https://alu-intranet.hbtn.io/status")
    
    # Check if the request was successful (status code 200)
    if r.status_code == 200:
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))  # Type of the response body (string)
        print("\t- content: {}".format(r.text))    # The content of the response (HTML as text)
    else:
        print("Request failed with status code:", r.status_code)
