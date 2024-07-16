class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        # U = return the number of groups of 1
        # M - DFS --> stack 
        # P - find a 1 and then search everywhere around it 
            # check if the current spot is valid to check!
            # if its a 1 --> conver to 0 and then search for more island (search everywhere around it and search everyhwere around those values --> DFS because going further and further into this path )
            # if its a 0 --> end this DFS search
        def dfs(grid, r, c):
            if (r < 0 or c<0 or r >= len(grid) or c >= len(grid[0])):
                # this spot is out of bounds so don't need to check anything
                return 
            if (grid[r][c] != "1"):
                # we reached water don't follow this path bc nowhere to go or already visited
                return 
            # turn this spot to -1 to say we already visited this node
            grid[r][c] = "-1"
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
        
        count  = 0 # counts the number of islands
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(grid, i, j)
        return count
