# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(inf, sup, tree):

            if not tree:
                return True
            
            sup_curr = tree.val
            left = dfs(inf, sup_curr, tree.left)
            inf_curr = tree.val
            right = dfs(inf_curr, sup, tree.right)
            
            print(inf, tree.val, sup)
            return left and right and inf < tree.val < sup
        
        return dfs(float("-inf"), float("inf"), root)
