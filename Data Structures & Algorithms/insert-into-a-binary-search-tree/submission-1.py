# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root

        curr = root
        parent = None
        while curr:
            parent = curr
            if val > root.val:
                curr = curr.right
            else:
                curr = curr.left
        
        if val > parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root
        


