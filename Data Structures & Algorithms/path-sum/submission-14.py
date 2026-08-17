# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(tree, cur_sum):
            if not tree:
                return False

            cur_sum += tree.val  # accumulate here

            if not tree.left and not tree.right:  # leaf node
                return cur_sum == targetSum

            return dfs(tree.left, cur_sum) or dfs(tree.right, cur_sum)

        return dfs(root, 0)
