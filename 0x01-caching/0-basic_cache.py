#!/usr/bin/python3
"""Defines a class called BasicCache that inherits from BaseCaching."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a caching system."""

    def put(self, key, item):
        """Assigns the dictionary self.cache_data the item value for the key.
        If the key or item is None, does nothing.
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """Returns the value in self.cache_date linked to key.
        If key is None or key doesn't exist in self.cache_data, returns None."""

        return self.cache_data.get(key)
