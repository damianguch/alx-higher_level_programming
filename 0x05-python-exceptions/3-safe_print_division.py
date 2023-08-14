#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        answer = a / b
        print("Inside result: {:.1f}".format(answer))
    except(TypeError, ZeroDivisionError):
        answer = None
        print("Inside result: {}".format(answer))
    finally:
        return answer
