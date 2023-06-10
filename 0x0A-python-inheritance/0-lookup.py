#!/usr/bin/python3
"""
Contains function lookup that returns a list of available  attributes and
methods of an object
"""


def lookup(obj):
    """returns list of object's attribute and methods"""
    return dir(obj)
