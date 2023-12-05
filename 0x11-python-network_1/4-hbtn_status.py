#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    requests = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response: ")
    print("\t- content: {}".format(requests.text))
    print("\t- type: {}".format(type(requests.text)))