class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pal(l, r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        curr = []
        def backtrack(i):

            if i >= len(s):
                res.append(curr[::])
                return
            
            for j in range(i, len(s)):
                if is_pal(i, j):
                    curr.append(s[i:j+1])
                    backtrack(j + 1)
                    curr.pop()
        
        backtrack(0)
        return res
