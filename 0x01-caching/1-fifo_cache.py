#!/usr/bin/env python3
"""
    A module to implement FIFO caching system
"""

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
            it with key and implement FIFO caching system
        """
        if key is None or item is None:
            pass

        cache = self.cache_data
        item_num = len(cache)
        max_items = BaseCaching.MAX_ITEMS
        if item_num >= max_items and key not in cache:
            print(f"DISCARD: {self.keys_array[0]}", end='\n')
            del cache[self.keys_array[0]]  # delete the first item
            del self.keys_array[0]  # then delete the first key

        self.keys_array.append(key)  # add the new key to the new array
        cache[key] = item  # add new item with key to the cache data

    def get(self, key):
        """
            returns the item in the cached data dict
            that is assigned to the key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
