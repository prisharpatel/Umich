class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # generate all combos of open and closed parentheses 

        # what is important = length of 2n, all open parentheses before closed ones
        output = []

        curPath = ""

        def backtrack(leftCount, rightCount, curPath):
            if len(curPath) == 2*n and leftCount == rightCount: 
                output.append(curPath)
                return 
            if leftCount < n: 
                curPath += "("
                backtrack(leftCount + 1, rightCount, curPath) 
                curPath = curPath[0:-1]
            if leftCount > rightCount:
                curPath += ")"
                backtrack(leftCount, rightCount + 1, curPath)
                curPath = curPath[0:-1]
            
        backtrack(0, 0, "")
        return output