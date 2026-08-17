class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pal(l, r):

            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        def backtrack(curr, idx):

            if idx >= len(s):
                res.append(curr[::])
                return
            
            for j in range(idx, len(s)):
                if is_pal(idx, j):
                    curr.append(s[idx:j+1])
                    backtrack(curr, j + 1)
                    curr.pop()
        
        backtrack([], 0)
        return res
            
