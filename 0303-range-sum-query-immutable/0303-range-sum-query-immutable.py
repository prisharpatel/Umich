class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # cache it
        for i in range(1, len(nums)): 
            nums[i] = nums[i] + nums[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right < len(self.nums):
            return self.nums[right+1] - self.nums[left-1]
        else:
            return self.nums[right+1]
        
        
        return output

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)