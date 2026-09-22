class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path_split = path.split("/")
        stack = []

        for p in path_split:
            if p == "":
                continue
            else:
                if p == ".":
                    continue
                if (p == "..") and stack:
                    stack.pop()
                elif p == ".." and not stack:
                    continue
                else:
                    stack.append(p)
        
        return "/" + "/".join(stack)