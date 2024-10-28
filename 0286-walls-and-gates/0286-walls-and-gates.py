class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # -1 = a wall or obstacle
        # 0 = a gate 
        # INF = empty room 

        # goal: fill each empty room with its distance to its nearest gate (0), if not possible, fill w INF 

        # matching - graphs, matrix, paths: shortest paths so bfs O(V+E) which means we are using queues 

        # pseudocode
        # go through the matrix m x n with double for loop (at least mxn time complexity)
            # if room = gate, go backwards on it and fill empty rooms with path distance
            # keep obstacles and gate as the values that they are so nothing for those 

        m = len(rooms)
        n = len(rooms[0])
        INF = 2147483647
        # bfs pseudo 
            # you have a position that you pop off the queue
            # add neighbors to a queue

        queue = deque()

        for row in range(m):
            for col in range(n): 
                if rooms[row][col] == 0: # we reached a gate
                    queue.append((row,col))
        
        # path = 0 
        visited = set()
        while queue: 
            r, c = queue.popleft()
            
            distance = rooms[r][c] + 1
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == INF:
                    rooms[nr][nc] = distance  # Set the distance from the nearest gate
                    queue.append((nr, nc))  
            

        return rooms

