# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(tree, l, r):

            if not tree:
                return True
            
            if l < tree.val < r:
                left = dfs(tree.left, l, min(r, tree.val))
                right = dfs(tree.right, max(l, tree.val), r)
                return left and right
            else:
                return False
        
        return dfs(root, float("-inf"), float("inf"))
