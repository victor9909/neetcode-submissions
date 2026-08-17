# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(start, end, tree):

            if not tree:
                return True
            
            if start < tree.val < end:
                return dfs(start, min(tree.val, end),tree.left) and dfs(max(start, tree.val), end, tree.right)
            else:
                return False
        
        return dfs(float("-inf"), float("inf"), root)