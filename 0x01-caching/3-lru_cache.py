#!/usr/bin/python3
"""
    A module to implement LRU caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
        A class for LRU caching system
    """
    def __init__(self) -> None:
        """ initialize using the super class"""
        super().__init__()
        self.keys_array = []
    
    def put(self, key, item):
        """
            insert an item with key into the cache
            and implement LRU caching system
        """
        if key is None or item is None:
            pass
        cache = self.cache_data
        length = len(cache)
        max_items = BaseCaching.MAX_ITEMS
        if length >= max_items and key not in cache:
            print(f"DISCARD: {self.keys_array[0]}", end="\n")
            del cache[self.keys_array[0]]
            del self.keys_array[0]
        if key in self.keys_array:
            del self.keys_array[self.keys_array.index(key)]
        self.keys_array.append(key)
        print(self.keys_array)
        self.cache_data[key] = item

    def get(self, key):
        """
            returns the value of the item linked to the key
        """
        if key is None and key not in self.cache_data:
            return None
        return self.cache_data[key]

