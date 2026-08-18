# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(tree):

            if not tree:
                return [True, 0]
            
            balanced_l, depth_l = dfs(tree.left)
            balanced_r, depth_r = dfs(tree.right)

            is_balanced = balanced_l and balanced_r and abs(depth_l - depth_r) <= 1
            depth = max(depth_l, depth_r) + 1
            return [is_balanced, depth]
        
        
        return dfs(root)[0]