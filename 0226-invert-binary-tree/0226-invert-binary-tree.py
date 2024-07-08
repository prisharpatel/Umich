# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # iterativley switch values from left side of the tree to right side of teh tree and vice versa
        # m - binary tree problem - go through tree in a level order traversal, recursion 
        # pseudocode: 
            # recursion: 
                # base case: left child or right child is null, swap the children  
                # else: recurse on left node, recurse on right node
        def recurse(node):
            if not node:
                return node
            
            temp = node.right
            node.right = node.left
            node.left = temp

            recurse(node.left)
            recurse(node.right)

        
        recurse(root)
        return root

            
        