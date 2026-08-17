class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()


        def backtrack(curr, curr_s, i):
            
            if curr_s == target:
                res.append(curr[::])
                return

            if curr_s > target or len(candidates) == i:
                return

            curr.append(candidates[i])
            backtrack(curr, curr_s + candidates[i], i + 1)
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(curr, curr_s, i + 1)
        
        backtrack([], 0, 0)
        return res