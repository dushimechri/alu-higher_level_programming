#!/usr/bin/python3
"""writing a function that reads a file"""


def read_file(filename=""):
"""now let's pass the code down below"""


    with open(filename, 'r',encording='UTF-8') as f:
        return f.read()
