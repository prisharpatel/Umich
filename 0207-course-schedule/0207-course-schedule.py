class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 
        # courses = 0 --> numCourses - 1 
        # prerequisites[i] = [ai, bi] means prerequisites[i][2] before prerequisites[i][1]

        # we can make hashmap to do this so its easier to understand and see which classes are 
        # required for another 

        # true if you can finish all courses and false otherwise 

        # matching - topological sorting... but can visualize as a graph...
        # cycle existing in directed graph if a cycle exists then it wont be possible to take all courses

        # graph: 
            # node: directed edges INTO IT 
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
        
        # see if there is a cycle in this graph? 
        # cycle means that to take course 1 you have to take course 2 and to take course 2 
        # you have to take course 1 so theres a cycle

        # cycle means you reach a visited node already when doing dfs
        # can have dif connected components though and its fine ... so just go through all nodes in range num courses
        # need to have an instack for this instance bc can't have entire visited set because if we did, it would mean 
        # that two pre reqs cant exist for two dif classes
        visited = set()

        # returns true if there is a cycle and false otherwise
        def dfs(i, inStack):
            if inStack[i]: # have a cycle bc have visited this already
                return True 
            if i in visited:
                return False
            
            # mark current node as visited and as part of the current stack
            inStack[i] = True
            visited.add(i)
            for prereq in graph[i]:
                if dfs(prereq, inStack):
                    return True # there is a cycle
            # remove the node from current recursion stack
            inStack[i] = False
            return False
        

        inStack = [False] * numCourses
        for i in range(numCourses):
            if dfs(i, inStack):
                return False # bc theres a cycle

        


        return len(visited) == numCourses            

        