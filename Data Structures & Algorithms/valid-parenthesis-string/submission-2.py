class Solution:
    def checkValidString(self, s: str) -> bool:
        
        #.       ( opn = 1 close = 0 i = 0
        #.       (( opn = 2 close = 0 i = 1
        #.      i = 2
        #.  3,0. 2,0.  2,1
        #.  (((. ((.   (()
               #.   3,1.  2,1.   2,2  i = 3
               #.  (()(. (().   (())
               #.   3,2.   2,2.    2,3 i = 4
               #.  (()).  (()).   (()))

        memo = {}

        def dfs(opn, i):
            
            if (i, opn) in memo:
                return memo[(i, opn)]

            if opn < 0:
                return False

            if i >= len(s):
                return opn == 0
        
            if s[i] == "(":
                memo[(i, opn)] = dfs(opn + 1, i + 1)
                return memo[(i, opn)]
            elif s[i] == ")":
                memo[(i, opn)] = dfs(opn - 1, i + 1)
                return memo[(i, opn)]
            else:
                memo[(i, opn)] = (
                    dfs(opn, i + 1) or
                    dfs(opn + 1, i + 1) or
                    dfs(opn - 1, i + 1)
                )
                return memo[(i, opn)]
        
        return dfs(0, 0)
        