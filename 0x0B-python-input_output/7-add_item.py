#!/usr/bin/python3
""" load and save json data"""
import sys
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

args = sys.argv[1:]

try:
    message = load_from_json_file("add_item.json")
except FileNotFoundError:
    message = []

    message.extend(args)
    save_to_json_file(message, "add_item.json")
