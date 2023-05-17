#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = matrix.copy()
    for _ in matrix_cpy:
        for i in _:
            print(i ** 2, end="")
        print()
