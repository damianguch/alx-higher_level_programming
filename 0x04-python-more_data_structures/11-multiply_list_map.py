#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    my_list_cpy = my_list.copy()
    return (list(map(lambda x: x * number, my_list_cpy)))
