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
            
            print(right, tree.val, left)
            if right <= tree.val <= left:
                return tree
            else:
                if tree.val <= right and tree.val <= left:
                    return dfs(tree.right, right, left)
                else:
                    return dfs(tree.left, right, left)
        
        right, left = min(p.val, q.val), max(p.val, q.val)
        return dfs(root, right, left)
            
