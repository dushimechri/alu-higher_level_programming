#!/usr/bin/python3
def uppercase(istr):
    result = ""
    for i in istr:
        if ord('a') <= ord(i) <= ord('z'):
            result += print("{}".format(chr(ord(i) - 32)
        else:
            result += i
    print("{}".format(result))

