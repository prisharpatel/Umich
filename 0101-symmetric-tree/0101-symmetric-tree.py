# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # goal: check if the nodes mirror each other which means the kids are on oppoiste sides, pattern with checking the tree recursivley as you go down  
        # matching - tree, level order, recursion

        # base case: 
            # node is null, return true
            # call recurse to check if the left child of the node is equal to the right child of the the other node
        output = True
        def recurse(node1, node2):
            if not node1 and not node2:
                return True # didn't get a false before and reached the bottom of the tree to checking symmetry
            if not node1 or not node2:
                return False # can't match because nodes don't align
            if node1.val == node2.val:
                return recurse(node1.left, node2.right) and recurse(node2.left, node1.right)

        return recurse(root.left, root.right)

        