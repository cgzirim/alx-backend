#!/usr/bin/python3
"""Defines a class LFUCache that inherits from BaseCaching."""

BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """Least frequently used (LFU) caching system."""

    def __init__(self):
        super().__init__()
        self.count = 0
        self.lru_count = {}
        self.lfu_count = {}

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item value of
        the key.
        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if len(self.lru_count) > 0:
            lru_key = self.get_lru()
            lfu_key = self.get_lfu()

        if key not in self.lru_count:
            self.lru_count.update({key: self.count})
            self.lfu_count.update({key: 0})
            self.count += 1
        else:
            self.lru_count.update({key: self.lru_count[key] + 1})
            self.lfu_count.update({key: self.lfu_count[key] + 1})

        self.cache_data.update({key: item})

        if len(self.cache_data) > self.MAX_ITEMS:
            if type(lfu_key) == list:
                self.lru_count.pop(lru_key)
                self.lfu_count.pop(lru_key)
                self.cache_data.pop(lru_key)
                print("Discard: {}".format(lru_key))
            else:
                self.lru_count.pop(lfu_key)
                self.lfu_count.pop(lfu_key)
                self.cache_data.pop(lfu_key)
                print("Discard: {}".format(lfu_key))

    def get(self, key):
        """Returns the value in self.cache_data linked to key."""
        if key in self.cache_data.keys():
            self.lru_count[key] = self.lru_count[key] + 1
            return self.cache_data.get(key)
        return None

    def get_lru(self):
        """Returns the least resently used key."""
        items = [(k, v) for k, v in self.lru_count.items()]
        items.sort(key=lambda item: item[1])
        duplicates = [item for item in items if item[1] == items[0][1]]
        if len(duplicates) > 1:
            return duplicates[-1][0]

        return items[0][0]

    def get_lfu(self):
        """Returns the least frequently used key(s)."""
        items = [(k, v) for k, v in self.lfu_count.items()]
        items.sort(key=lambda item: item[1])
        duplicates = [item for item in items if item[1] == items[0][1]]
        if len(duplicates) > 1:
            return duplicates

        return items[0][0]
