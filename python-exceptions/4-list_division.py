#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
              # Check if both lists have elements at index i
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)
            else:
                results = my_list_1[i] / my_list_2[i]
                result.append(results)
    except ZeroDivisionError:
        print("division by 0")
        result.append(0)
    except TypeError:
        print("wrong type")
        result.append(0)
    except IndexError:
        print("out of range")
        result.append(0)
    finally:
        return result
