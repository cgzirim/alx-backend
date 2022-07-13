#!/usr/bin/env python3
""" LFUCache Module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Class Implementing LFU"""

    def __int__(self):
        """ class constructor"""
        super().__init__()
    use_count = {}

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value of
        the key.
        If key or item is None, this method does nothing.
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                itemKeyToDiscard = \
                    sorted(self.use_count.items(), key=lambda x: x[1])[0][0]

                self.cache_data.pop(itemKeyToDiscard)
                self.use_count.pop(itemKeyToDiscard)
                print('DISCARD: {}'.format(itemKeyToDiscard))
            if not self.use_count.get(key):
                self.use_count[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key."""
        if key:
            if self.use_count.get(key) is not None:
                self.use_count[key] += 1
            return self.cache_data.get(key)