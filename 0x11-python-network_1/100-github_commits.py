#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/User"(sys.argv[2], sys.argv[1])
    request = requests.get(url)
    commits = requests.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha")))
    except:
        raise ValueError("")
