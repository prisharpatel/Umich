class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return k closest points to the origin based on euclidean distance which means we 
        # want k minimum distances 
        # which is max heap of k distances
        # EX: 
        # distances are 1, 2, 5
        # we find one that is 4 

        # distances are -5, -2, -1
        # we find one that is -4 which is smaller than largest distnac e
        # -4 -2 -1 
        heap = []
        for i, point in enumerate(points): 
            x = point[0]
            y = point[1]
            distance = sqrt(x**2 + y**2)

            if len(heap) == k and heap[0][0] * -1 > distance:
                heapq.heappop(heap)    
                heapq.heappush(heap, (distance * -1, i))
            elif len(heap) < k: 
                heapq.heappush(heap, (distance * -1, i))

        # O(K)
        output = []
        for dist, point in heap: 
            output.append(points[point])

        return output

        
        