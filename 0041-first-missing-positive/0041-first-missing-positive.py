class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        maxVal = max(nums)
        while i in nums and i < len(nums)+1:
            i += 1
        if i == len(nums):
            return len(nums) 
        return i 

        

        