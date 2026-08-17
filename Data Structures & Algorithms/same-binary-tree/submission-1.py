# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #   1           
        # 2   3
        
        #    1
        #  2   3
        # 4

        def dfs(tree_p, tree_q):

            if not tree_p and not tree_q:
                return True
            
            if tree_p and tree_q and tree_p.val == tree_q.val:
                left = dfs(tree_p.left, tree_q.left)
                right = dfs(tree_p.right, tree_q.right)
                return left and right
            else:
                return False
        
        return dfs(p, q)
            

