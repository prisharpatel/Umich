class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        maxVal = max(nums)
        while i in nums and i < maxVal:
            i += 1
        if i == maxVal:
            return maxVal + 1 
        return i 

        

        