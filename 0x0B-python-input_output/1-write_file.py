#!/usr/bin/python3

"""
function "wrtie_file"
"""
def write_file(filename="", text=""):
    """return num of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)