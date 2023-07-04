#!/usr/bin/python3

"""
    a Python script that takes in a URL
    sends a request to the URL
    displays the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    url = sys.argv[1]
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as er:
        print('Error code:', er.code, 'Reason:', er.reason)
