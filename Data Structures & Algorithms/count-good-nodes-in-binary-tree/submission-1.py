# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def dfs(tree, value):
            nonlocal res

            if not tree:
                return
            
            if value <= tree.val:
                res += 1
            
            val_to_pass = max(value, tree.val)
            dfs(tree.left, val_to_pass)
            dfs(tree.right, val_to_pass)
        
        dfs(root, root.val)

        return res