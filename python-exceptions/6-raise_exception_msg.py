#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError:
        print(message)

raise_exception_msg("C is fun")
