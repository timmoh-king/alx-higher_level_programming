#!/usr/bin/python3

""" a script that adds all arguments to a Python list"""
import json
import os.path
import sys
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_list = []

if os.path.exists(filename):
    my_list = load_from_json_file(filename)

for i in argv[1:]:
    my_list.append(i)

save_to_json_file(my_list, filename)
