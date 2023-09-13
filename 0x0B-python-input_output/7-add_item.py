#!/usr/bin/python3
"""add all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    mList = load_from_json_file(filename)
except Exception:
    mList = []

for i in range(len(sys.argv)):
    if i == 0:
        continue
    mList.append(sys.argv[i])

save_to_json_file(mList, filename)
