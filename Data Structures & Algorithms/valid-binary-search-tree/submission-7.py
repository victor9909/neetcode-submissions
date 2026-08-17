# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(tree, left, right):

            if not tree:
                return True
            
            if left < tree.val < right:
                left_n = max(tree.val, left)
                right_n = min(tree.val, right)
                return dfs(tree.left, left, right_n) and dfs(tree.right, left_n, right)
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))