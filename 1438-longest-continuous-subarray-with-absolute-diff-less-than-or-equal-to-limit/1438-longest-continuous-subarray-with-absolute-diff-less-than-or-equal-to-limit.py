from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque, minDeque = deque(), deque()
        left = 0
        maxLength = 0

        for right in range(len(nums)):
            # Maintain the max deque
            while maxDeque and nums[maxDeque[-1]] < nums[right]:
                maxDeque.pop()
            maxDeque.append(right)

            # Maintain the min deque
            while minDeque and nums[minDeque[-1]] > nums[right]:
                minDeque.pop()
            minDeque.append(right)

            # Check if the current window is valid
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                left += 1  # Move the left pointer to shrink the window
                # Remove elements outside the window from deques
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()

            # Update max length of a valid window
            maxLength = max(maxLength, right - left + 1)

        return maxLength
