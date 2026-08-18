# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(min_val, max_val, tree):

            if not tree:
                return True
            
            if min_val < tree.val < max_val:
                left = dfs(min_val, min(max_val, tree.val), tree.left)
                right = dfs(max(min_val, tree.val), max_val, tree.right)
                return left and right
            else:
                return False
        
        return dfs(float("-inf"), float("inf"), root)