#!/usr/bin/python3
"""define function that returns the list of available
attributes and methods of an object."""


def lookup(obj):
    """return list object"""
    return (dir(obj))
