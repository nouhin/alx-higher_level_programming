#!/usr/bin/python3
for alphabet in range(97, 123):
    if chr(alphabet) != 'e' and chr(alphabet) != 'q':
        print("{:c}".format(alphabet), end="")
