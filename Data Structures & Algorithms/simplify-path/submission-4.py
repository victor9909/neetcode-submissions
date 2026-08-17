class Solution:
    def simplifyPath(self, path: str) -> str:
        # "/neetcode/practice//...///../courses"
        # ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        # /neetcode/practice/courses/

        # "/..//"
        # ['', ..,'', '']
        # /

        # "/..//_home/a/b/..///"
        # ['', '..', '', '_home', 'a', 'b', '..', '', '', '']
        # /_home/a/b

        stack = []
        path_arr = path.split('/')
        for p in path_arr:
            if (p == ".." ) and stack:
                stack.pop()
            elif p == "":
                continue
            elif p == "" or (p == ".." and not stack) or p == ".":
                continue
            else:
                stack.append('/' + p)
        
        return ''.join(stack) if stack else '/'

        

        


        