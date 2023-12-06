import collections


class LRU:
    """ Least Recently Used Cache """

    def __init__(self, capacity: int):
        """ Initialize cache to store data

        :param capacity: cache size
        """
        self.remaining = capacity
        self.lru_cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        """ Return the value of key in cache
        :param key: Search key
        :return: Value
        """
        if key in self.lru_cache:
            value = self.lru_cache.pop(key)
            self.lru_cache[key] = value
            return value
        return -1

    def add(self, key: int, value: int) -> None:
        """ Add value in cache if not exists otherwise update the current value
        :param key: Cache Key
        :param value: Cache Value
        :return:
        """
        if key in self.lru_cache:
            self.lru_cache.pop(key)
        elif self.remaining == 0:
            self.lru_cache.popitem(last=False)
        else:
            self.remaining -= 1
        self.lru_cache[key] = value


if __name__ == "__main__":
    cache = LRU(3)
    print(cache.get(2))  # Expected: -1
    cache.add(2, 1)
    print(cache.get(2))  # Expected: 1
    cache.add(3, 1)
    cache.add(4, 2)
    cache.add(5, 3)
    cache.add(6, 4)
    print(cache.get(2))  # Expected: -1
