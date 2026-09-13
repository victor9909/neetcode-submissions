# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        def dfs(tree, prev):

            if not tree:
                return 0
            
            cnt = 0
            if tree.val >= prev:
                cnt += 1
            
            left = dfs(tree.left, max(prev, tree.val))
            right = dfs(tree.right, max(prev, tree.val))

            return left + right + cnt
        
        return dfs(root, root.val)
