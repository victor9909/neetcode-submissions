# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def dfs(tree, max_val):
            
            nonlocal res
            if not tree:
                return
            
            max_curr = max(max_val, tree.val)
            if tree.val >= max_curr:
                res += 1 
            dfs(tree.left, max_curr)
            dfs(tree.right, max_curr)

        dfs(root, float("-inf"))

        return res

