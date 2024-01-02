#!/usr/bin/python3
"""
module to get a header variable
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_var = response.getheader("X-Request-Id")
        print(x_var)
