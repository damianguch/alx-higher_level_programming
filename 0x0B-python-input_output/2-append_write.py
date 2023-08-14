#!/usr/bin/python3
"""
Module contains a function that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends to text file and returns num chars added"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
