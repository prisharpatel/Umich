class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # U - given an sorted unique integer arrray
        # return the smallest sorted list of ranges that cover all numbers in the array

        # M - while loops, arrays
        # Pseudocode:   
            # while within while
                # within that check if need to add to output one value or arrow
        output = []
        i = 0 
        while i < len(nums):
            start = i
            while  i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
            if start == i:
                output.append(str(nums[i]))
            else:
                output.append(str(nums[start]) + "->" + str(nums[i]))
            i += 1
            
        return output