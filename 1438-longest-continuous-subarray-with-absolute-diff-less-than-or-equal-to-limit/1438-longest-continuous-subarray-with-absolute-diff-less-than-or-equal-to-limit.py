from typing import List
import heapq
from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap, maxHeap = [], []
        remove_map = defaultdict(int)
        left = 0
        maxLength = 0

        for right in range(len(nums)):
            # Add current element to both heaps
            heapq.heappush(minHeap, (nums[right], right))
            heapq.heappush(maxHeap, (-nums[right], right))

            # Ensure the current window's max-min is within the limit
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                # Increment count of elements to remove for lazy deletion
                remove_map[nums[left]] += 1
                left += 1  # Move the left pointer to shrink the window

                # Clean up the minHeap for elements outside the window
                while minHeap and remove_map[minHeap[0][0]] > 0:
                    value, idx = heapq.heappop(minHeap)
                    remove_map[value] -= 1

                # Clean up the maxHeap for elements outside the window
                while maxHeap and remove_map[-maxHeap[0][0]] > 0:
                    value, idx = heapq.heappop(maxHeap)
                    remove_map[-value] -= 1

            # Update the max length of a valid window
            maxLength = max(maxLength, right - left + 1)

        return maxLength
