#!/usr/bin/env python3
""" Basic cache class """


BaseCaching = __import__('base_caching').BaseCaching
class BasicCache(BaseCaching):
    """ BasicCache class """
    def __init__(self):
        """ Constructor """
        super().__init__()
