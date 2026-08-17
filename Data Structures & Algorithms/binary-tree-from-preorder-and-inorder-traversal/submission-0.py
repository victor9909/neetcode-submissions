# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        dict_idx = {}

        for i, n in enumerate(inorder):
            dict_idx[n] = i

        def build_tree(preorder: List[int], inorder: List[int]):
            if not preorder or not inorder:
                return None
            
            root = TreeNode(preorder[0])
            idx = dict_idx[preorder[0]]
            root.left = self.buildTree(preorder[1: idx+1], inorder[:idx])
            root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

            return root
        
        return build_tree(preorder, inorder)