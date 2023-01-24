#!/usr/bin/env python3
"""
    A module to implement FIFO caching system
"""
from os import remove


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        a class that implements FIFO caching system
    """
    def __init__(self):
        """
            initialize using the super cleass
        """
        super().__init__()
        self.keys_array = []

    def put(self, key, item):
        """
            puts the item in the cached data after assigning
            it with key
        """
        if key is None or item is None:
            pass

        item_num = len(self.cache_data)
        max_items = BaseCaching.MAX_ITEMS
        if item_num >= max_items and key not in self.cache_data:
            print(f"DISCARD: {self.keys_array[0]}", end='\n')
            del self.cache_data[self.keys_array[0]]  # delete the first item
            del self.keys_array[0]  # then delete the first key

        self.keys_array.append(key)  # add the new key to the new array
        self.cache_data[key] = item  # add new item with key to the cache data

    def get(self, key):
        """
            returns the item in the cached data dict
            that is assigned to the key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]