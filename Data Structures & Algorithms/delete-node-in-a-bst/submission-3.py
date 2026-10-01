# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:

            if not root.left and not root.right:
                return None
            
            if(
                root.left and not root.right or
                root.right and not root.left
            ):
                return root.left or root.right
            
            curr = root.right
            while curr.left:
                curr = curr.left
            
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)

        return root

