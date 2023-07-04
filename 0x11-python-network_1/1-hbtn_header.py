#!/usr/bin/python3

"""
    a Python script that takes in a URL, sends a request to the URL
    displays the value of the X-Request-Id variable
    found in the header of the response.
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers_dict = dict(response.getheaders())
        print(headers_dict['X-Request-Id'])
