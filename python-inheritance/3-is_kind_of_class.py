#!/usr/bin/python3

""" Function that returns True if the object is an instance
or if the object is an instance of a class that
inherited from the specified class."""


def is_kind_of_class(obj, a_class):
    """Checks what kind of class."""
    return isinstance(obj, a_class)
