class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def backtrack(num, curr):

            if len(curr) == k:
                res.append(curr[::])
                return

            if num > n:
                return
            
            curr.append(num)
            backtrack(num + 1, curr)
            curr.pop()
            backtrack(num + 1, curr)
        
        backtrack(1, [])
        return res
