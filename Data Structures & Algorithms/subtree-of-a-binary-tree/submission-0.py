# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(p, q):

            if not p and not q:
                return True
            
            if p and q and p.val == q.val:
                return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
            else:
                return False
        
        if not root and subRoot:
            return False
        
        if not subRoot and root:
            return True
        
        if is_same_tree(root, subRoot):
            return True
        
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

            
