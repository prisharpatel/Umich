class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return true if element appearing in list 
        # create set - check if set as long as nums (o(N))
        # have to have it be at lesat O(N) because otherwise you can't go through all elements 
        # ==> can't optimize 
        return len(nums) != len(set(nums))
        