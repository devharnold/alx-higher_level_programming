#!/usr/bin/python3
"""
the json str function
"""

import json

def from_json_string(my_str):
    """return object represented by a JSON string"""
    return json.loads(my_str)