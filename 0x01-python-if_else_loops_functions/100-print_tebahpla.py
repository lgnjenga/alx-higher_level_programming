#!/usr/bin/python3
for i in range(122, 96, -2):
    print("{}".format(chr(i)), end="")
    if i != 97:
        print("{}".format(chr(i - 33)), end="")
