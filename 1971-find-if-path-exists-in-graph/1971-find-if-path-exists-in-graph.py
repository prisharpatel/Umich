class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # can you get from source to destination  given edges
        # bidirectional so when looking for edge in edges look for s, d and d, s

        # match - valid path so dfs which means stacks and visited neighbor list 

        # psuedo code 
        stack = deque([source]) # stack to use to go through nodes you can try to visit with nodes
        visited = set() # O(1) access
        # have a while loop for stack() being not empty
        # in while loop iteration, look at current node and
        # 1) check if node == destination - return true 
        # 2) look through edges and if the edge[0] or edge[1] = currentNode and the opposite one not in visited 
        # then add it to the stack to epxlore

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        while stack: 
            currentNode = stack.popleft() # can be in here because stack guaranteed to have at least one becuase of condition 
            
            if currentNode == destination:
                return True # path found

            if currentNode not in visited:
                visited.add(currentNode)
                if currentNode in graph:
                    for neighbor in graph[currentNode]:
                        if neighbor not in visited:
                            stack.appendleft(neighbor)
                    

        return False

        