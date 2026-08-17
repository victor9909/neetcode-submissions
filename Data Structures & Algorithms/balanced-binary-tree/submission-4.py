# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(tree: Optional[TreeNode]) -> (bool, int):

            if not tree:
                return (True, 0)
            
            balanced_l, left_h = dfs(tree.left)
            balanced_r, right_h = dfs(tree.right)

            is_balanced = balanced_l and balanced_r and abs(left_h - right_h) <= 1
            height = max(left_h, right_h) + 1

            return (is_balanced, height)
        
        return dfs(root)[0]

