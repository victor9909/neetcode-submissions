# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []
        def dfs(tree):

            if not tree:
                res.append("N")
                return 
            
            res.append(str(tree.val))
            dfs(tree.left)
            dfs(tree.right)
        
        dfs(root)
        return "#".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        arr = data.split("#")
        i = 0

        def dfs():
            nonlocal i
            if arr[i] == "N":
                return None
            
            tree = TreeNode(int(arr[i]))
            i += 1
            tree.left = dfs()
            i += 1
            tree.right = dfs()

            return tree
        
        return dfs()
