class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs with backtracking 
        if board is None:
            return 
        m = len(board)
        n = len(board[0])
        visited = set()
        
        def dfs(r, c, i): 
            if i == len(word):
                return True 
            if 0 <= r < m and 0 <= c < n and i <len(word): 
                if board[r][c] != word[i] or (r,c) in visited:
                    return False
                visited.add((r,c))
                res = dfs(r+1, c, i + 1) or dfs(r-1, c, i + 1) or dfs(r, c+1, i + 1) or dfs(r, c-1, i + 1) 
                visited.remove((r,c ))
                return res
                
            else: 
                return False 

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:  #some optimization 
                    if dfs(r, c, 0):# only do this if grid letter starts with the first letter of the word
                        return True 

        return False
        