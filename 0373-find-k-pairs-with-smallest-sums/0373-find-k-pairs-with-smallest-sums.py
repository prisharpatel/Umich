class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
       

        # u = with two arrays, find the smallest sums between one element from each array
        # match - find minimum pairs so heap to keep track of minimum pairs
        # p 
            # first smallest pair always giong to be the first two values of nums1 and nums2
            # second smallest pair going to be the sum of nums1[0] + nums2[1] or nums1[1] + nums2[0] --> keep adding pairs to the minHeap by finding k pairs --> guaranteed to have increasing amount of sums becuase sorted in nondecreasing order
        
        output = []
        #output.append((nums1[0], nums2[0]))
        if k==1:
            return output
        
        minHeap = [(nums1[0]+nums2[0], (0, 0))]
        visited = set()
        visited.add((0, 0))
        count= 0
        while count < k and minHeap:
            val, (i, j) = heappop(minHeap)
            output.append((nums1[i], nums2[j]))

            # add next values to minHeap so that the smallest ones can be added eventually to output
            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heappush(minHeap, (nums1[i+1] + nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                heappush(minHeap,  (nums1[i] + nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
            count +=1 
        return output


