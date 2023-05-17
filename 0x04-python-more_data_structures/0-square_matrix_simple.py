#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for _ in matrix:
        for i in _:
            print(i ** 2, end="")
        print()
