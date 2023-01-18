#!/usr/bin/python3

"""This is a script that takes in a URL,
- sends a request to the URL and displays the body of the response
- manage urllib.error.HTTPError
- exceptions and print: Error code
- followed by the HTTP status code
"""

import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error

    try:
        with urllib.request.urlopen(sys.argv[1]) as req:
            print(req.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
