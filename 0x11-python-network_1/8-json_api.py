#!/usr/bin/python3

"""A script that takes ina letter and sends a post request to
- http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import urllib.request

def searchapi():
    if len(sys.argv) == 1:
        q = ""
    else:
        sys.argv[1]

    result = request.post("http://0.0.0.0:5000/search_user", data = {"q": q})

    data = result.json

    try:
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    searchapi()
