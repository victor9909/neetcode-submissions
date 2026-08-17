# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(tree):

            if not tree:
                return
            
            tree.right, tree.left = dfs(tree.left), dfs(tree.right)
            return tree
        
        return dfs(root)