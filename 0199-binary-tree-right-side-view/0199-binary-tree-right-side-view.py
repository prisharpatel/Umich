# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: # tree is empty
            return []

        q = [root]
        output = [root.val]
        
        while len(q) > 0:
            levelNodes = []
            # adding nodes of level from left to right
            for node in q:
                if node.left:
                    levelNodes.append(node.left)
                if node.right:
                    levelNodes.append(node.right)
            
            # append last one to output
            if len(levelNodes) > 0:
                output.append(levelNodes[-1].val)
            
            # add to q, the nodes that are in this level
            q = levelNodes
        return output
        