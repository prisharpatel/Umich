class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return all the triplets that sum to 0 
        # sort nums 

        nums.sort() # 3 takes less space complecity then strted 
        lastNum = None
        output = []
        for i, num in enumerate(nums): 
            if lastNum == num: 
                continue
            lastNum = num

            left = i + 1
            right = len(nums)-1
            while left < right: 
                s = nums[left] + nums[right]
                if s + num == 0: 
                    output.append([num, nums[left], nums[right]])
                    right -=1 
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                elif s + num < 0: 
                    # need a larger number to offset 
                    left += 1
                else: 
                    right -= 1
        
        return output
            
        