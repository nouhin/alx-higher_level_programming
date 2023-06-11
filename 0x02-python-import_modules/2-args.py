#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)
    args = sys.argv[1:]
    if num_args == 1:
        print("0 arguments.")
    elif num_args == 2:
        print("1 argument:")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(num_args - 1))
        for i, arg in enumerate(args):
            print("{}: {}".format(i + 1, arg))
