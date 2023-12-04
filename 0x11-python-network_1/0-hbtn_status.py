#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
