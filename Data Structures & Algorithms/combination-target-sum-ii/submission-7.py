class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []

        def backtrack(i, curr, curr_s):

            if curr_s == target:
                res.append(curr[::])
                return
            
            if i >= len(candidates) or curr_s > target:
                return
            
            curr.append(candidates[i])
            backtrack(i + 1, curr, curr_s + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            curr.pop()
            backtrack(i + 1, curr, curr_s)
        
        backtrack(0, [], 0)
        return res
            
