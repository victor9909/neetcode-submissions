# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def check_leaf(tree):

            if not tree:
                return False
            
            if tree.val == target and not tree.left and not tree.right:
                return True
            
            return check_leaf(tree.left) or check_leaf(tree.right)

        def dfs(tree):

            if not tree:
                return None
            
            if tree.val == target and not tree.left and not tree.right:
                return None
            
            tree.left = dfs(tree.left)
            tree.right = dfs(tree.right)

            return tree
        
        while check_leaf(root) and root:
            root = dfs(root)
        
        return root
