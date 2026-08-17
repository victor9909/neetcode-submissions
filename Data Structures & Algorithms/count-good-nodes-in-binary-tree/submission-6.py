# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(tree: TreeNode, max_path: int):

            if not tree:
                return 0
            
            left = dfs(tree.left, max(tree.val, max_path))
            right = dfs(tree.right, max(tree.val, max_path))

            return left + right + (1 if tree.val >= max_path else 0)
        
        #return dfs(root, root.val)

        q = deque()
        q.append((root, root.val))
        res = 1

        while q:
            len_q = len(q)
            for _ in range(len_q):
                node, max_p = q.popleft()
                if node.left:
                    res += 1 if node.left.val >= max_p else 0
                    q.append((node.left, max(node.left.val, max_p)))
                if node.right:
                    res += 1 if node.right.val >= max_p else 0
                    q.append((node.right, max(node.right.val, max_p)))
        
        return res
                


