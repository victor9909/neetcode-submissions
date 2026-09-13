# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same(l, r):

            if not l and not r:
                return True
            
            if not l or not r:
                return False
            
            if l and r and l.val == r.val:
                return is_same(l.left, r.left) and is_same(l.right, r.right)
            else:
                return False
        
        if not root and subRoot:
            return False
        
        if root and not subRoot:
            return True
        
        if not is_same(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return True
