#!/usr/bin/python3
"""Defines a class FIFOCache that inherits from BaseCaching."""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A caching system."""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value of
        the key.
        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return 

        self.cache_data.update({key: item})

        if len(self.cache_data) > self.MAX_ITEMS:
            ord_dict = OrderedDict(self.cache_data)
            k_v = ord_dict.popitem(last = False)
            del self.cache_data[k_v[0]]
            print("DISCARD: {}".format(k_v[0]))
            

    def get(self, key):
        """Returns the value in self.cache_data linked to key."""
        return self.cache_data.get(key)
