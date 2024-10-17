class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums is an array sorted in increasing order 
        # nums MAY BE rotated at an unknown pivot index so sorting might be off and we need to resort it 
        # algo must be in log(n) time complexity --> binary search 
        
        # matching - binary search, array 

        # pseudocode: 
        # 1) find how many spots array was rotated by finding minimum value using binary search 
            # if nums[mid] > nums[-1] --> pivot value on right 
            # if nums[mid] < nums[-1] --> pivot value on left 
        # 2)  perform binary search of two sorted arrays from 0 to pivot index and pivotindex + 1 to end

        # 1) 
        start, end = 0, len(nums)-1
        while start <= end:
            middle = start + end-start//2

            if nums[middle] > nums[-1]:
                # pivot value on right
                start = middle + 1
            else:
                
                end = middle - 1
            
        # pivot = left index 
        # binary search of left array
        def binarySearch(nums: List[int], target: int, left: int, right:int):
            while left <= right: 
                middle = left + (right-left) // 2
                if target < nums[middle]: 
                    # on left 
                    right = middle -1
                elif target > nums[middle]:
                    # on right 
                    left = middle + 1
                else: return middle
            return -1

        leftArr = binarySearch(nums, target, 0, start-1)
        if leftArr != -1:
            return leftArr
        rightArr = binarySearch(nums, target, start, len(nums)-1)
        if rightArr != -1:
            return rightArr
        return -1


