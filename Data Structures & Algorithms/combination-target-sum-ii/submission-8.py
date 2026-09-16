class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        curr = []

        def backtrack(i, curr_s):

            if curr_s == target:
                res.append(curr[::])
                return
            
            if curr_s > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            backtrack(i + 1, curr_s + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            backtrack(i + 1, curr_s)
        
        backtrack(0, 0)
        return res