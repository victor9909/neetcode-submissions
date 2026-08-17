# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def dfs(tree, right, left):

            if not tree:
                return None
            
            if right <= tree.val <= left:
                return tree
            else:
                if tree.val <= right and tree.val <= left:
                    return dfs(tree.right, right, left)
                else:
                    return dfs(tree.left, right, left)
        
        curr = root
        right, left = min(p.val, q.val), max(p.val, q.val)
        while curr:
            if right <= curr.val <= left:
                return curr
            elif curr.val <= p.val and curr.val <= q.val:
                curr = curr.right
            else:
                curr = curr.left

        #right, left = min(p.val, q.val), max(p.val, q.val)
        #return dfs(root, right, left)
            
