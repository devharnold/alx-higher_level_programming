#!/usr/bin/python3
"""Takes URL, sends a request to the URL and displays
the body of the response(decoded in "utf-8")
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))

