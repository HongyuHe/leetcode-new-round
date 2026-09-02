from collections import defaultdict
import heapq as hq
class LRUCache:
    """
    Attempt 1, 38min
    Plan:
        * Use dict for the cache
        * Use a min heap for LRU key
        * Keep a record of the latest timestamps, and discard any ts < updated value
        * Have an monotonically increasing var to represent "time" (max 2*10^5)
    """

    def __init__(self, capacity: int):
        self.ts = -1
        self.cap = capacity
        self.hascap = True
        self.updates = defaultdict(int)
        self.lru_keys = []
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Update the timestamps
        self.ts += 1
        self.updates[key] = self.ts
        # Touch key
        hq.heappush(self.lru_keys, (self.ts, key))
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # Update the timestamps
        self.ts += 1
        self.updates[key] = self.ts
        # Insert the key
        hq.heappush(self.lru_keys, (self.ts, key))

        # Updating existing values
        if key in self.cache:
            self.cache[key] = value
            return

        # Adding new values
        self.cache[key] = value
        # Checking capcity
        if self.hascap:
            if len(self.cache) == self.cap:
                self.hascap = False
        else:
            # Do eviction
            lru_key = None
            while True:
                key_ts, lru_key = hq.heappop(self.lru_keys)
                if key_ts < self.updates[lru_key]:
                    # Outdated value, skip
                    continue
                else:
                    break
            assert lru_key is not None
            del self.cache[lru_key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)