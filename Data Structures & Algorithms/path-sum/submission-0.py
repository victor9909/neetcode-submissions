# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack(tree, cur_sum):

            if not tree:
                return False
            
            curSum = cur_sum + tree.val
            is_leaf = not tree.left and not tree.right
            if curSum == targetSum and is_leaf:
                return True
            
            res = backtrack(tree.left, curSum) or backtrack(tree.right, curSum)
            return res

        return backtrack(root, 0)

        