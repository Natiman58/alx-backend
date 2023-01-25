#!/usr/bin/env python3
"""
    A module to implement MRU (Most recently used) caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ A class to implement MRU caching system """
    def __init__(self):
        """initialize using the super class"""
        super().__init__()
        self.keys_array = []

    def put(self, key, item):
        """Put an an item in to the cache using the given key"""
        if key is None or item is None:
            pass
        else:
            cache = self.cache_data
            cache_len = len(cache)
            max_item_len = BaseCaching.MAX_ITEMS
            if cache_len >= max_item_len and key not in cache.keys():
                last_key = self.keys_array[-1]
                print(f"DISCARD: {last_key}", end='\n')
                del cache[last_key]  # delete item linked to the key from cache
                del last_key  # finally delete the key from the keys array

            if key in self.keys_array:  # if key is in the cache & keys array
                del self.keys_array[self.keys_array.index(key)]
            self.keys_array.append(key)  # add the new key into array of keys
            cache[key] = item  # and assign that key to an item

    def get(self, key):
        """
            return the value of the item linked to the key
        """
        if key is not None and key in self.cache_data.keys():
            del self.keys_array[self.keys_array.index(key)]
            self.keys_array.append(key)
            print(self.keys_array)
            return self.cache_data[key]
        return None
