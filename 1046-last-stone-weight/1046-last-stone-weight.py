class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap which means we need to make stone weights negative 
        max_heap = []
        for stone in stones: 
            max_heap.append(-1*stone)
        
        heapq.heapify(max_heap)

        while len(max_heap) > 1: 
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)

            if x != y: 
                y = x - y 
                heapq.heappush(max_heap, y*-1)
        
        if len(max_heap) == 0:
            return 0 
        else:
            return heapq.heappop(max_heap) * -1
        