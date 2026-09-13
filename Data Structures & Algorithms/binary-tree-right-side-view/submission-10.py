# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        res.append(root.val)

        while q:
            len_q = len(q)
            node_r = None
            for _ in range(len_q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    node_r = node.left.val
                if node.right:
                    q.append(node.right)
                    node_r = node.right.val
            if node_r:
                res.append(node_r)
        return res
                