from collections import defaultdict

class TimeMap:
    """
    Attempts:
        1. 30m
    Requirements:
        * Mulitple values per key
        * Timestamp the values 
        * Return the latest value given a ts

    Plan:
        * Storage: dict[list[tuple(value, ts))]]
        * Search: binary search
    Questions:
        * Multiple items of the same value AND ts?
    """

    def __init__(self):
        self.db = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.db[key]
        if not values:
            return ""
        
        #* Do binary search
        '''
        [(red, 0), (green, 2)]: get(0)
        [(red, 0), (green, 2), (blue, 3)]: get(4)
        '''
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            value, ts = values[mid]
            if ts == timestamp:
                return value
            
            if ts < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        #* Didn't find the exact timestamp, return the closet previous one
        if right >= 0:
            return values[right][0]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)