# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def isBalanced(root, cnt):

            if not root:
                return [True, 0]
            
            left = isBalanced(root.left, cnt + 1)
            right = isBalanced(root.right, cnt + 1)

            print(abs(left[1] - right[1]))
            is_balanced = abs(left[1] - right[1]) <= 1 and right[0] and left[0]

            return (is_balanced, max(left[1], right[1]) + 1)
        
        return isBalanced(root, 0)[0]

