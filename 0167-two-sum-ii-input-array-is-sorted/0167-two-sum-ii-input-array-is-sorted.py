class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted in ascending order 
        # find two numbers such that they add up to target and index1 < index2 

        # can't use hashmap/hashset bc cant use extra space

        # sorted so binary search thing with two pointers

        left = 0 
        right = len(numbers)-1
        while left < right: 
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s > target: 
                right -=1 
            else: 
                left += 1
        
        