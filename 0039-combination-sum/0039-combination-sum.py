class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # return a list of unique combinations of candidates where the chosen numbers sum to target 

        # can choose the same number from candidates an unlimited number of times
        output = []# set of sets
        curPath = []

        def dfs(curPath, curSum, start): 
            if curSum > target:
                return 

            if curSum == target and set(curPath) not in output:
                output.append(list(curPath))
                return 
                
            
            # try adding all to the current path 
            for i in range(start, len(candidates)): 
                num = candidates[i]
                curPath.append(num)
                curSum += num
                dfs(curPath, curSum, i)
                curPath.pop()
                curSum -= num

        dfs([], 0, 0)            

        # go through
        return output
            
        