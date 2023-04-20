#!/usr/bin/env python3
"""
module contains BasicCache class that inherits from BaseCaching
that caches data in a dictionary
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits and stores.
    """
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        add item to cache.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.keys:
                    val = self.keys[0]
                    del self.cache_data[self.keys[0]]
                    del self.keys[0]
                    print('DISCARD:', val)
                else:
                    self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)
            if key in self.keys[:-1]:
                self.keys.remove(key)

    def get(self, key):
        """
        return value linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.keys.remove(key)
        self.keys.append(key)
        return self.cache_data[key]
