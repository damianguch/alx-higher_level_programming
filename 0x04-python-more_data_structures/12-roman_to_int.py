#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    n = 0
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i, j in zip(roman_string, roman_string[1:]):
        if i not in d.keys():
            return 0
        elif d[i] >= d[j]:
            n += d[i]
        else:
            n -= d[i]
    n += d[roman_string[-1]]

    return n
