#!/usr/bin/env python3
"""
    A module to implement LIFO caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
        A class for LIFO cache
    """
    def __init__(self):
        """
            initialize using the parent class
        """
        super().__init__()
        self.keys_array = []

    def put(self, key, item):
        """
            to put an item into the cache data linked to a key
            and implement LIFO caching system
        """
        if key is None or item is None:
            pass
        else:
            cache = self.cache_data
            item_num = len(cache)
            max_items = BaseCaching.MAX_ITEMS
            if item_num >= max_items and key not in cache:
                print(f"DISCARD: {self.keys_array[-1]}", end='\n')
                del cache[self.keys_array[-1]]
                del self.keys_array[-1]
            if key in self.keys_array:
                del self.keys_array[self.keys_array.index(key)]
            self.keys_array.append(key)
            cache[key] = item

    def get(self, key):
        """
            return the value of the item linked to the key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return  None
