class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # array sorted in ascneding order 
        start, end = 0, len(nums)-1
        
        while start <= end: 
            middle = start + (end-start) // 2
            
            if nums[middle] > target: # will be on left
                end = middle - 1
                
            elif nums[middle] < target: # will be on right
                
                start = middle + 1
            else:
                return middle # middle is target
        return -1

        