class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 = EMPTY 
        # 1 = FRESH ORANGE
        # 2 = ROTTEN ORANGE

        # if fresh orange surrounded by rotten oranges, so if 1 surounded by 2's above, right, left, below
                # 1 --> 2
        # 4 directions, so if orange rotten on border, return -1 

        # graph, matrix, bfs because as things get rotten can add to a queue any neighbors that aren't 
        # rotten to see if they can be made rotten later

        # psuedo 
        # bfs so queue = deque()
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # check if every fresh orange has at least one orange next to it in some direction
        
        # queue = deque()
        new_queue = deque()
        m = len(grid)
        n = len(grid[0])
        fresh_exist = False
        not_all_empty = False # assume all empty
        fresh_oranges = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # check border and make sure there is an orange around it
                    not_all_empty = True
                    fresh_exist = True
                    found = False
                    fresh_oranges += 1
                    for dr, dc in d:
                        nr, nc = r+dr, c+dc 
                        if nr >= 0 and nr < m and nc >= 0 and nc < n: 
                            if grid[nr][nc] == 1 or grid[nr][nc] == 2:
                                found = True
                                break
                    if not found:
                        return -1 # bc there is an orange that cannot become rotten
                if grid[r][c] == 2:
                    not_all_empty = True
                    new_queue.append((r,c))
        # if only 0's don't need a minute 
        if not not_all_empty: 
            return 0
        # len(new_queue) means there are twos 
        # 
        if len(new_queue) == 0:
            return -1
        # for each iteration
            # add all rotten oranges to a queue and check surroundings of it and make it rotten if its fresh
            # any fresh orange around it turns rotton and is added to the queue 
            
        # one minute
        count = 0 
        while new_queue:
            count += 1
            queue = new_queue
            new_queue = deque()
            changed = False
            while queue: # ADD SOME CONDITION for minutes 
                r, c = queue.popleft() 
                for dr, dc in d:
                    nr, nc = r+dr, c+dc 
                    if nr >= 0 and nr < m and nc >= 0 and nc < n: 
                        if grid[nr][nc] == 1:
                            fresh_oranges-=1
                            changed = True
                            grid[nr][nc] = 2
                            new_queue.append((nr,nc))
            
        if fresh_oranges != 0:
            return -1
        else:
            return count -1 




        # check if there are any fresh oranges left and if they can become rotten???
            

        