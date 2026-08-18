# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(tree, max_par):

            if not tree:
                return 0
            
            cnt = 0
            if tree.val >= max_par:
                cnt += 1
            
            left = dfs(tree.left, max(tree.val, max_par))
            right = dfs(tree.right, max(tree.val, max_par))

            return left + right + cnt
        
        return dfs(root, root.val)