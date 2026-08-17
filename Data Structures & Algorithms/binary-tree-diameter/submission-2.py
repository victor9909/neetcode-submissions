# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(root, cnt):
            nonlocal res
            if not root:
                return 0

            left = dfs(root.left, cnt + 1)
            right = dfs(root.right, cnt + 1)
            
            res = max(res, left + right)

            return max(left, right) + 1
        
        dfs(root, 0)
        return res
