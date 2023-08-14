#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arguments_sum = 0
    for i in range(len(argv) - 1):
        arguments_sum += int(argv[i + 1])
    print("{}".format(arguments_sum))
