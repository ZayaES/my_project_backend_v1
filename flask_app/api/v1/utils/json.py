#!/usr/bin/python3

import json


def read_json(filename):
    """ reads a json file
        
        arg: (string) url to file
        return: loaded json content 
                or empty list if file not found
    """

    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    return data


def write_json(filename, data):
    """ writes data to json file 
        args: (string) url to file
              (list of object) data to write to file
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def append_json(filename, new_data):
    """ appends new data onto existing json_file
        args: (string) url to file
                (list) new data to append to json file

    """
    data = read_json(filename)
    data.append(new_data)
    write_json(filename, data)
