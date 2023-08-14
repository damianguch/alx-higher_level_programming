#!/usr/bin/python3
import magic_calculation_102


def magic_calculation(a, b):
    c = 0
    if a < b:
        c = magic_calculation_102.add(a, b)
        for i in range(4, 6):
            c = magic_calculation_102.add(c, i)
    else:
        c = magic_calculation_102.sub(a, b)
    return c
