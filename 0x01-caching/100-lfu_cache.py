#!/usr/bin/env python3
"""
    A module to implement LFU (Least-frequently used) caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ A class to implement LFU caching system

    Args:
        BaseCaching: Super class: 
    """
    def __init__(self):
        """ initialize the class using the super class """
        super().__init__()
        self.keys_array = []

    def put(self, key, item):
        """ puts an item into the cache"""
        if key is None or item is None:
            return None
        else:
            cache = self.cache_data
            cache_len = len(cache)
            num_items = BaseCaching.MAX_ITEMS
            
            if num_items >= cache_len and key not in cache:
                print(f"DISCARD: {''}", end="\n")
            