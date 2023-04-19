#!/usr/bin/env python3
"""
module contains BasicCache class that inherits from BaseCaching
that caches data in a dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class adds and retrieves data items from a dictionary
    """

    def __init__(self):
        """
        initializes a new base class object
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        function adds items to a dictionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        function retieves items from a dictionary
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
