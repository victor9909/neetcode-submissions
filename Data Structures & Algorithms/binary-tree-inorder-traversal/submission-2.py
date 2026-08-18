# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def dfs(tree):

            if not tree:
                return
            
            dfs(tree.left)
            res.append(tree.val)
            dfs(tree.right)
        
        dfs(root)
        return res
        