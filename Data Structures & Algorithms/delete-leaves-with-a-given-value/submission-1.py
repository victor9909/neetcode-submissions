# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        dummy = TreeNode(-1, left = root)

        def dfs(tree):

            if not tree:
                return False
            
            
            left = dfs(tree.left)
            right = dfs(tree.right)

            if left:
                tree.left = None
            if right:
                tree.right = None

            return tree.val == target and not tree.left and not tree.right
        
        dfs(dummy)

        return dummy.left
