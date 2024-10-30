#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end=' ')
            count += 1
    except IndexError:
        pass 
    except TypeError:
        print("put x as number")
    except NameError:
        print("try again")

    finally:
        print("nb_print:{}".format(count))
