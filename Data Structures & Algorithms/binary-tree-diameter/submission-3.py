# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(tree):
            nonlocal res

            if not tree:
                return 0
            
            left = dfs(tree.left)
            right = dfs(tree.right)
            res = max(res, left + right)

            return max(left, right) + 1
        
        dfs(root)
        return res