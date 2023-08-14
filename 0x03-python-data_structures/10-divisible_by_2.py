#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_vals = []
    length = len(my_list)
    for i in range(length):
        if my_list[i] % 2 == 0:
            bool_vals.append(True)
        else:
            bool_vals.append(False)

    return (bool_vals)
