# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = defaultdict(list)


        def dfs(tree, level):
            
            if not tree:
                return
            res[level].append(tree.val)
            dfs(tree.left, level + 1)
            dfs(tree.right, level + 1)
        
        dfs(root, 0)
        return list(res.values())
