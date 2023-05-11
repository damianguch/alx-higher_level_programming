def magic_calculation(a, b):
    add, sub = __import__('magic_calculation_102', globals(), locals(), ['add', 'sub'], 0)
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)


#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for n in range(4, 6):
            c = add(c, n)
        return c
    else:
        return sub(a, b)


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

