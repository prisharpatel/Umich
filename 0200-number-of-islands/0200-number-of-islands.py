class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 = land
        # 0 = water 
        rows = len(grid)
        cols = len(grid[0])
        # return the number of islands 

        # matching - dfs

        # psuedocode 
        visited = set() # set of tuples for ordered pairs 
        islandSize = 0
        stack = deque() # pop left() and appendleft() - add tuples of places
        count = 0

        # see what triggers dfs and add that many to count 

        
        def dfs(i, j): 
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1" or (i, j) in visited:
                return 
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
                    
        

        return count

        