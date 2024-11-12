#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r',encording='UTF-8') as f:
        return f.read()
