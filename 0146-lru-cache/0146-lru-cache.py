class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # dictionary that stores key --> value 
        self.limit = capacity
        self.LRU = [] # LRU is at index 0 of this
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # update LRU 
            if key in self.LRU:
                self.LRU.remove(key)
            self.LRU.append(key) 
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #  if cache size = to limit
            # pop off index 0 from LRU and remove that value/key pair from cache 
        # add new key/value pair to cache 
        # FOLLOW UP: CAN THE SAME KEY BE INPUTTED TWO TIMES TO THE CACHE? 
        # check if key in cache already 
        
        if len(self.cache) == self.limit and key not in self.cache: 
            lru = self.LRU.pop(0) 
            # how can we gaurantee that lru is in the cache?
            # only add to lru if it is put into the cache and remove now 
            self.cache.pop(lru)
        self.cache[key] = value
        if key in self.LRU: 
            self.LRU.remove(key)
        self.LRU.append(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)