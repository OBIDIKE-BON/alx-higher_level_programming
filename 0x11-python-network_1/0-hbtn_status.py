#!/usr/bin/python3
"""
module that downloads url
"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(f"Body response:\n\t- type: {type(html)}")
        print(f"\t- content: {html}\n\t- utf8 content: {html.decode('utf-8')}")
