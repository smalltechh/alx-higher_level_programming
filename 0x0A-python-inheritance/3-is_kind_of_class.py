#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Returns: True if object is an instance of a class that inherited
     from, the specified class ; otherwise False."""
    if isinstance(obj, a_class):
        return True
    return False
