"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # given a node that is connected to all other nodes, need to make a deep copy, so need to make a new node and make new connections/set values the same
        # going through adjacency matrix --> bfs (look through node and its neighbors first)
        # copy first node
        # create a list of neighbors from node 
        # recurse on each neighbor node

        visited = {}

        def recurse(node):
            if node is None:
                return None

            if node.val in visited:
                return visited[node.val]
            
            newNode = Node(node.val)

            visited[node.val] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(recurse(neighbor))
                
            return newNode
        return recurse(node)

        