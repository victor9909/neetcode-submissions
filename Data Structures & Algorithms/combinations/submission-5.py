class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def backtrack(e, curr):

            if len(curr) == k:
                res.append(curr[::])
                return
            
            if e > n:
                return
            
            curr.append(e)
            backtrack(e + 1, curr)
            curr.pop()
            backtrack(e + 1, curr)
        
        backtrack(1, [])
        return res