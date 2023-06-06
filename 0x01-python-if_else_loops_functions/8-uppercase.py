#!/usr/bin/python3
def uppercase(char):
    print("".join([
        chr(ord(c) - 32) if ord(c) >= 97 and ord(c) <= 122 else c
        for c in char
    ]).format())
