#!/usr/bin/python3
"""that adds all arguments to a Python list"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arglist = list(sys.argv[1:])

try:
    json_list = load_from_json_file('add_item.json')

except Exception:
    json_list = []

json_list.extend(arglist)

save_to_json_file(json_list, 'add_item.json')
