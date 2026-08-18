class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        pos = {v: i for i, v in enumerate(inorder)}
        pre = 0

        def dfs(left, right):
            nonlocal pre

            if left > right:
                return None

            root_val = preorder[pre]
            pre += 1

            root = TreeNode(root_val)

            mid = pos[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)