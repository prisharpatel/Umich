class Solution:
    def climbStairs(self, n: int) -> int:
        # takes n steps to reach the top of a staircase 
        # can either climb one or two steps so how many dif ways can u climb to the top

        # dynamic programming
        # base case 
        # n = 0 --> 0 
        # n = 1 --> 1 
        
        # recursive case 
        # f(n) = f(n-1) (add 1 staircase step to all those solutions) + f(n-2) (add two staircase steps to all those solutions)

        memo = {1: 1, 2:2}
        if n in memo:
            return memo[n]
        else:
            for i in range(3, n+1):
                memo[i] = memo[i - 1] + memo[i-2]
        return memo[n]
        