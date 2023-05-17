#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        sum_unique_int = 0
        unique_list = set(my_list)

        for item in unique_list:
            sum_unique_int += item

        return (sum_unique_int)
    return None
