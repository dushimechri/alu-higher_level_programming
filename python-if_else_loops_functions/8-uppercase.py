#!/usr/bin/python3
def uppercase(istr):
    result = ""
    for i in istr:
        if 'a' <= i <= 'z':
            result += chr(ord(i) - 32)
        else:
            result += i
    return result

