#!/usr/bin/python3
"""This functioin adds arguments to python list
and write them into the json file
"""
from sys import argv

if __name__ == "__main__":
    save_to_json_file = __import__(
            "5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__(
            "6-load_from_json_file").load_from_json_file

    try:
        jsonList = load_from_json_file("add_item.json")
    except FileNotFoundError:
        jsonList = []

    jsonList.extend(argv[1:])

    save_to_json_file(jsonList, "add_item.json")
