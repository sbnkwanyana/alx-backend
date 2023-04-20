#!/usr/bin/env python3
"""
module contains BasicCache class that inherits from BaseCaching
that caches data in a dictionary
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits and stores.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        add item to cache.
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.last_key)
                print('DISCARD:', self.last_key)
            if key:
                self.last_key = key

    def get(self, key):
        """
        return value linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
