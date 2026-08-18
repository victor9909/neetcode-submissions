# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        q.append(root)

        if not root:
            return []

        res = []
        res.append([root.val])
        while q:
            len_q = len(q)
            level = []
            for _ in range(len_q):
                node = q.popleft()
                if node.left:
                    level.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    level.append(node.right.val)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
