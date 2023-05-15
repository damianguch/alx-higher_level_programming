#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        bool_val = []
        for item in my_list:
            if item % 2 is 0:
                bool_val.append(True)
            else:
                bool_val.append(False)
        return bool_val
