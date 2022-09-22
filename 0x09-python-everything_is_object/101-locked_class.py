#!/usr/bin/python3
class LockedClass:
    """ Defines a class that prevents the user from dynamicallh creating new instances of attributes except if the new attribute is called first_name
    """
    __slots__ = ['first_name']
