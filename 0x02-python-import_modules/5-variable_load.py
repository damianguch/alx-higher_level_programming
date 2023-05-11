if __name__ == "__main__":
    # import the variable 'a' from the file 'variable_load_5.py'
    from variable_load_5 import a

    # print the value of 'a'
    print(a)

#!/usr/bin/python3
from variable_load_5 import a


def find_var():
    print(a)


if __name__ == "__main__":
    find_var()
