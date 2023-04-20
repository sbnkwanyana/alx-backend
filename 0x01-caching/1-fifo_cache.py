#!/usr/bin/env python3
"""
module contains BasicCache class that inherits from BaseCaching
that caches data in a dictionary
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class was genrated by AI as a test and it works perfectly
    with no modifications to the code. Im worried

    """
    def __init__(self):
        """
        """
        super().__init__()

    def put(self, key, item):
        """
        The put method assigns the value of the item to
        the dictionary self.cache_data for the key key.
        If either the key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, we discard the first item put in cache using
        the FIFO algorithm and print out a message indicating
        which key was discarded.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")
        self.cache_data[key] = item

    def get(self, key):
        """
        The get method returns the value in self.cache_data
        linked to the key. If the key is None
        or if the key doesn’t exist in self.cache_data, it returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
