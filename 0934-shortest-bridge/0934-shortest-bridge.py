class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # n x n binary matrix 
        # 1 = LAND, 0 = WATER 

        # two islands in grid 
        # connect the two islands

        # matching - bfs?? 
        # understand: shortest path between two 1's that aren't connected already 
        # 0  1
        # 1  0 

        # 0  1  0 
        # 0  0  0 
        # 0  0  1

        # [1,1,1,1,1]
        # [1,0,0,0,1]
        # [1,0,1,0,1]
        # [1,0,0,0,1]
        # [1,1,1,1,1]

        # psuedo code
        # matching: bfs because shortest path

        # pseudocode: 
        # we need to separate the two islands because we aren't going to be able to tell which island is which 
        # go through cells starting at [0, 0] and when you find a 1 convert all ones connected to 2's

        # using queues bc this is bfs
        if grid is None:
            return None

        m = len(grid)
        n = len(grid[0])

        # direcs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
             
        first_x, first_y = -1, -1
        
        # Find any land cell, and we treat it as a cell of island A.
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    found = True
                    break
            if found:
                break
        
        # bfsQueue for BFS on land cells of island A; secondBfsQueue for BFS on water cells.
        bfs_queue = [(first_x, first_y)]
        second_bfs_queue = [(first_x, first_y)]
        grid[first_x][first_y] = 2
        
        # BFS for all land cells of island A and add them to second_bfs_queue.
        while bfs_queue:
            new_bfs = []
            for x, y in bfs_queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
                        new_bfs.append((cur_x, cur_y))
                        second_bfs_queue.append((cur_x, cur_y))
                        grid[cur_x][cur_y] = 2
            bfs_queue = new_bfs

        distance = 0
        while second_bfs_queue:
            new_bfs = []
            for x, y in second_bfs_queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            new_bfs.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1

            # Once we finish one round without finding land cells of island B, we will
            # start the next round on all water cells that are 1 cell further away from
            # island A and increment the distance by 1.
            second_bfs_queue = new_bfs
            distance += 1