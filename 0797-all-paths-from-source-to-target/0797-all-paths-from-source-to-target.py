class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # find all paths from 0 to n-1
        # root = 0 and destination = n-1

        # matching - dfs -- any path not shortest path 

        # pseudocode: 
        # access O(1) because know array index 
        # call dfs starting on 0 
        # explore neighbors and see if any of them are n-1 
        # if not, add them to the currentpath, call dfs, pop off currentpath  

        if graph is None:
            return None
        output = []
        visited = set()
        n = len(graph)

        def dfs(curPath, node):
            if node == n-1:
                # reached end of path 
                # curPath.append(node)
                output.append(list(curPath))
                return 
            
            for neighbor in graph[node]:
                curPath.append(neighbor)
                dfs(curPath, neighbor)
                curPath.pop()
            return 
        
        dfs([0], 0)
        return output

            