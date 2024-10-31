class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}
        for i in range(len(nums)): 
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            want = target - nums[i]
            if want in hashmap and hashmap[want] != i: 
                return [i, hashmap[want]]
        return -1
        