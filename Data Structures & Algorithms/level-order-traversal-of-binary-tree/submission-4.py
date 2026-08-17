# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dict_levels = defaultdict(list)

        def dfs(tree, level):

            if not tree:
                return
            
            dict_levels[level].append(tree.val)
            dfs(tree.left, level + 1)
            dfs(tree.right, level + 1)
        
        if not root:
            return []

        dfs(root, 0)
        n_levels = max(dict_levels.keys())
        res = []
        for i in range(n_levels + 1):
            res.append(dict_levels[i])
        return res




        q = deque()
        q.append(root)
        res = []
        
        if not root:
            return []

        while q:
            len_q = len(q)
            level = []
            for _ in range(len_q):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(level) >= 1:
                res.append(level[::])
        
        return res
