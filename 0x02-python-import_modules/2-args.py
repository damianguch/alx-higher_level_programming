#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_count = len(argv) - 1
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))
    for i in range(arg_count):
        print("{}: {}".format(i + 1, argv[i + 1]))
