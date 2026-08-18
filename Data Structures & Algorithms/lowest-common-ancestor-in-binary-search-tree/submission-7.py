# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(tree):

            if not tree:
                return None
            
            if tree.val == p or tree.val == q:
                return tree

            if min(p.val, q.val) > tree.val:
                return dfs(tree.right)
            elif max(p.val, q.val) < tree.val:
                return dfs(tree.left)
            else:
                return tree
        
        return dfs(root)

