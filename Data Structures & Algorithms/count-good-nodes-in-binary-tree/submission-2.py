# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = 0

        def dfs(tree, parent):
            
            nonlocal good

            if not tree:
                return 
            
            if tree.val >= parent:
                good += 1
            
            dfs(tree.left, max(tree.val, parent))
            dfs(tree.right, max(tree.val, parent))
        
        dfs(root, root.val)
        return good

