class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # return all possible subsets from nums including []
        
        # 2^n bc each element can be in set or not 

        # match - backtracking 
        output = []
        def backtrack(i, curPath): # curPath is the current combo rn and i is the first element to consider adding
            if i == len(nums):
                output.append(curPath.copy())
                return 
            # add number and go down that path 
            curPath.append(nums[i])
            backtrack(i+1, curPath)

            # don't add number and go down that path 
            curPath.pop()
            backtrack(i+1, curPath)

            return 

        backtrack(0, [])

        return output

            


        