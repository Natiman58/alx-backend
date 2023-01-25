#!/usr/bin/env python3
"""
    A base class module
"""
# BaseCaching = __import__('base_caching').BaseCaching
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        A base class that inherit from base cache class
    """
    def __init__(self):
        """
            initialize this class using the parent class
        """
        super().__init__()

    def put(self, key, item):
        """
            Assigns the item to the key
            and add the item to the cached data dict
            if no key or item; dont print anythiing
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
            returns the value associated with the assigned key
            from the cached data dict
            if there is no key or key is not in the dict return None
        """
        if key is None and key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
