#!/usr/bin/python3
"""
Module contains a function that writes a string to a text file and returns
the number of characers written
"""


def write_file(filename="", text=""):
    """writes to text file and returns num chars written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
