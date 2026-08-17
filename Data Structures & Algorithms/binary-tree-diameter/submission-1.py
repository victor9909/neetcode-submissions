# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0


        def dfs(tree, curr):
            nonlocal res
            if not tree:
                return 0
            
            left = dfs(tree.left, curr + 1)
            right = dfs(tree.right, curr + 1)
            res = max(left + right, res)

            return max(left, right) + 1

        dfs(root, 0)
        return res
            