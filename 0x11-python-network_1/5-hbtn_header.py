#!/usr/bin/python3
"""
Send request to URL and display the value of the variable X-Request-Id
in the response header
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
