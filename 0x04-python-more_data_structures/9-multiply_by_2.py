#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        dict = {}
        mul_dict = {}
        for key, value in a_dictionary.items():
            new_val = value * 2
            mul_dict = {key: new_val}
            dict.update(mul_dict)
        return (dict)
    return None
