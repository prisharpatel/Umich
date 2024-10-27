class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # rooms labeled 0 to n-1 
        # 1 --> n-1 locked with key 
        # rooms[i] contains all the keys in each room 
        # return true if u can go to room 0 and then find keys in rooms that that room unlocks

        # do we need this?? -no 
        # unlocked = len(rooms) * [False]
        # unlocked[0] = True 

        # matching - dfs becuase you want to get to all rooms so follow path down with keys you have 

        visited = set() # index of rooms you have visited - starts with visiting 0 
        stack = deque([0])

        while stack:
            current_room = stack.popleft()
            # see if you have visited this room 
            if current_room not in visited: 
                visited.add(current_room)
                # add keys in here to the stack 
                for key in rooms[current_room]:
                    stack.appendleft(key)

                # 

        if len(visited) == len(rooms):
            return True
        else:
            return False


            



        dfs(rooms[0])

        