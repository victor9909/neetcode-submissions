# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(tree, curr):

            if not tree:
                return curr
            
            depth_left = dfs(tree.left, curr + 1)
            depth_right = dfs(tree.right, curr + 1)
            
            return max(depth_left, depth_right)

        return dfs(root, 0)

