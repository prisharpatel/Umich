# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        # all paths = analyzing structure = dfs

        output = []

        # dfs means backtrack bc looking for a path 

        def backtrack(node, curPath):
            if node is None:
                return 
            curPath += f"->{node.val}"
            if node.left is None and node.right is None: # reached a leaf
                output.append(curPath[2:]) # 2 because don't want first arrow
                return 
            backtrack(node.left, curPath)
            backtrack(node.right, curPath)

        
        
        backtrack(root, "")

        return output