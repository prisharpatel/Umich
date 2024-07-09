# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # goal: determine if a tree is height balanced
        # height balanced - depth of two subtrees of every node never differs by more than one 
        # matching - trees, level order traversal, recursion
        # pseudocode
            # base case - node has no children - return True becuase that means this node's subtree is balanced
            # recursive case -
                # recurse on node.left and node.right and check if they are balanced 
                # if the difference between the depths of subtrees is less than 1, return true, else false 
                # to check depth, need a function to check the height of the current subtree
        def height(node):
            # base case
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            else: # 2 children so return height of the larger subtree
                val = max(height(node.left), height(node.right)) + 1
                return val
                
        def recurse(node):
            if node is None:
                return True
            return abs(height(node.left) - height(node.right)) <= 1 and recurse(node.left) and recurse(node.right)
                
        return recurse(root)