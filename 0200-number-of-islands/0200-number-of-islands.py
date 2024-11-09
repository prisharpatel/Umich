class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 = land 
        # 0 = water 
        # return the number of islands

        # dfs

        # pseudocode
        # keep track of visited 
        visited = set() # add coordinates 
        # see if there is an island at every single spot as long as its not in visited and is a 1
        m = len(grid)
        n = len(grid[0])
        def dfs(r, c):
            if not (0 <= r < m) or not (0 <= c < n) or grid[r][c] == "0" or (r,c) in visited:
                return 
            
            visited.add((r,c))
            # call dfs on neighbors
            # grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1

        return islands
            

            

            
        