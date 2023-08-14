#!/usr/bin/python3
"""
Module contains function that reads  contents from a text file and prints
it to the stdout
"""


def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
