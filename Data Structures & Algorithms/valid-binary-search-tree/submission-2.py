# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def is_valid_bst(min_val, max_val, node):

            if not node:
                return True
            
            left = is_valid_bst(min_val, min(node.val, max_val), node.left)
            right = is_valid_bst(max(min_val, node.val), max_val, node.right)


            return left and right and min_val < node.val < max_val
        
        return is_valid_bst(float("-inf"), float("inf"), root)