#!/usr/bin/python3
"""function that check if the object is an instance of, or if the object is an
 instance of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """return True if the object is an instance or False in otherwise"""
    if (isinstance(obj, a_class)):
        return (True)
    return (False)
