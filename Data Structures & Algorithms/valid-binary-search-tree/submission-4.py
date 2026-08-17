# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(tree, min_v, max_v):

            if not tree:
                return True
            
            if min_v < tree.val < max_v:
                new_min = max(min_v, tree.val)
                new_max = min(max_v, tree.val)
                left = dfs(tree.left, min_v, new_max)
                right = dfs(tree.right, new_min, max_v)
                return left and right
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))