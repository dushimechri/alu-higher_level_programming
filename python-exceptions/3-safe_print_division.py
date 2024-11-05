#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
        print(f"Inside result: {result}")
    except ZeroDivisionError:
        print("None")
    finally:
        print("{:d} / {:d} = {}".format(a, b, result))
