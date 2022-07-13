#!/usr/bin/python3
"""Defines a class LIFOCache that inherits from BaseCaching."""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A Last In First Out (LIFO) caching system."""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value of
        the key.
        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        keys = [k for k in self.cache_data.keys()]

        self.cache_data.update({key: item})

        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[keys[-1]]
            print("DISCARD: {}".format(keys[-1]))


    def get(self, key):
        """Returns the value in self.cache_data linked to key."""
        return self.cache_data.get(key)
