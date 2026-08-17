# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(tree, curr):

            nonlocal res

            if not tree:
                res = max(res, curr)
                return
            
            dfs(tree.left, curr + 1)
            dfs(tree.right, curr + 1)

        dfs(root, 0)
        return res