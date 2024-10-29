class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru = deque() # most recently used on right side, so pop from left to get LRU

    def get(self, key: int) -> int:
        # use .remove() to remove and add to back of lru 
        
        if key in self.cache:
            self.lru.remove(key)
            self.lru.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # to track least recently 
        if key in self.cache:
            self.cache[key] = value

        if len(self.cache.keys()) == self.capacity and key not in self.cache:
            # remove lru 
            val = self.lru.popleft() 
            self.cache.pop(val, None)
        elif key in self.cache:
            self.lru.remove(key)
        # add new key
        self.cache[key] = value 
        # add to LRU
        self.lru.append(key)
            
        


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)