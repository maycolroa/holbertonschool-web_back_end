#!/usr/bin/env python3
"""
methods
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache
    """

    def put(self, key, item):
        """
        dictionary
        """
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
