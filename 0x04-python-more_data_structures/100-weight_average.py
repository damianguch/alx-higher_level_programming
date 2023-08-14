#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total = 0
        freq = 0
        for t in my_list:
            (score, weight) = t
            total += (score * weight)
            freq += weight
        return (total/freq) if freq > 0 else 0

    return (0)
