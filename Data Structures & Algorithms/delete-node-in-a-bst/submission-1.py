# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def findMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        def deleteNode(tree, val):

            if not tree:
                return tree
            
            if val > tree.val:
                tree.right = deleteNode(tree.right, val)
            elif val < tree.val:
                tree.left = deleteNode(tree.left, val)
            else:
                if not tree.left:
                    return tree.right
                elif not tree.right:
                    return tree.left
                else:
                    min_val = findMin(tree.right)
                    tree.val = min_val.val
                    tree.right = deleteNode(tree.right, min_val.val)
            return tree

        return deleteNode(root, key)








