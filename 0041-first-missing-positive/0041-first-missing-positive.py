class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = set(nums)
        # i = 1
        # maxVal = max(nums)
        # while i in nums and i < len(nums)+1:
        #     i += 1
        # if i == len(nums):
        #     return len(nums) 
        # return i 

        # use nums as a hashset of proviing if a number exists in array by turning it to a negative value if 
        # value exists at i - 1 index (EX: 1 exists if nums[0] is negative)

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            val = abs(nums[i])
            # edit the array to a negative number at pos i - 1 if it isn't already 
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = len(nums) + 1
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i 
        return len(nums) + 1

       

        

        