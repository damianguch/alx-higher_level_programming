#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for x in my_string:
        if x not in "cC":
            result += x
    return result
