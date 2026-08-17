# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(tree, curr_dep):

            if not tree:
                return 0
            
            right = dfs(tree.right, curr_dep + 1)
            left = dfs(tree.left, curr_dep + 1)

            return max(left, right) + 1
        
        return dfs(root, 1)