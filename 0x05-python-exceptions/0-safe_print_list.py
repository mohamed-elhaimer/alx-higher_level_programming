#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x < 0:
            print("Invalid value for x. Please provide a positive integer.")
        else:
            count = 0
        for item in my_list:
            if count < x:
                print("{}".format(item), end="")
                count += 1
            else:
                break
        print('')
        if (x > count):
            return (count)
        return (x)
    except Exception as e:
        print("{}".format(e))
