class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # combinations that exist wiht the digits given with corresponding letters 
        # worst case: 4^n where n = len(digits)? 
        
        # matching - dfs / backtracking

        # pseudocode: 
        # make some type of remembering what numbers connect to what letters -- hashmap
        dictionary = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'], 
            "4": ['g', 'h', 'i'], 
            "5": ['j', 'k', 'l'], 
            "6": ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'], 
            "9": ['w', 'x', 'y', 'z']
        }
        output = []
        if len(digits) == 0:
            return []
        def dfs(curPath, i): # where i represents spot in the digits u are in 
            if i == len(digits):
                output.append(curPath)
                return
            digit = digits[i]
            for val in dictionary[digit]: 
                curPath += val
                dfs(curPath, i+1)
                curPath = curPath[0:-1]
        dfs("", 0)
        return output        