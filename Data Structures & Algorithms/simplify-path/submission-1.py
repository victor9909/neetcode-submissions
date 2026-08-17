class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # /neetcode/practice//...///../courses
        # /neetcode/practice/.../../courses
        # [ neetcode, 'practice', '...', '..', courses]
        # [neetcode, practice, courses] -> /neetcode/practice/courses

        # path = "/..//"
        # /../
        # ['', .., '']
        # [..] -> /

        # "/..//_home/a/b/..///"
        # /../_home/a/b/../
        # ['', .., '_home', a, b, .., '']
        # [.., _home, a, b, ..] -> _home, a, -> /_home/a

        path = re.sub(r"/+", "/", path)
        arr_path = path.split("/")
        print(arr_path)
        stack = []
        for p in arr_path:
            if p == "":
                continue

            if stack and p == "..":
                stack.pop()
                continue
            if not stack and p == "..":
                continue
            if p == ".":
                continue
            stack.append(p)
        
        return "/" + "/".join(stack)
            
       