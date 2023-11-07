#!/usr/bin/python3
"""function that check if the object is exactly
 an instance of the specified class """


def is_same_class(obj, a_class):
    """return True if object is instance or False in otherwise"""
    if type(obj) == a_class:
        return (True)
    return (False)
