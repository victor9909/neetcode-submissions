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
            
            bl, hl = dfs(tree.left)
            br, hr = dfs(tree.right)
            balanced = bl and br and abs(hl - hr) <= 1
            
            return [balanced, max(hl, hr) + 1]
        
        return dfs(root)[0]