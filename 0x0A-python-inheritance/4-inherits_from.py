#!/usr/bin/python3
"""function that return if the object is an instance of a class that inherited
 (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Return True if is an instance of class that
      inherited from the specified class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
