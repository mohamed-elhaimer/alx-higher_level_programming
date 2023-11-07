#!/usr/bin/python3
"""define a subclass MyList"""


class MyList(list):
    """represent MyList"""
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
