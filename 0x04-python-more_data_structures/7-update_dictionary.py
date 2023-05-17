#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        d = {key: value}
        a_dictionary.update(d)
        return(a_dictionary)

    return None
