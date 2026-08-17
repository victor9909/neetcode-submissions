# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # 1
         # 2
       # 3  4 
       # 5 
        res = 0
        def dfs(tree):
            nonlocal res
            if not tree:
                return 0

            left_depth = dfs(tree.left)
            right_depth = dfs(tree.right)
            res = max(res, left_depth + right_depth)
            return max(left_depth,  right_depth) + 1

        dfs(root) 
        return res
    
        