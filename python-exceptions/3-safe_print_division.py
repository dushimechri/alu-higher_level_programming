#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        result = "None"
    finally:
        print(f"Inside result: {result}")
        print("{:d} / {:d} = {}".format(a, b, result))
