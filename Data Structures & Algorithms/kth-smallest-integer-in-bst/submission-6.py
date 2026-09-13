# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        s = []
        
        def dfs(tree):

            if not tree:
                return
            
            dfs(tree.left)
            s.append(tree.val)
            dfs(tree.right)
        
        dfs(root)
        return s[k - 1] if s else None
