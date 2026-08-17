class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtrack(idx, curr, curr_s):

            if target == curr_s:
                res.append(curr[::])
                return
            
            if idx >= len(candidates) or curr_s > target:
                return
            
            curr.append(candidates[idx])
            backtrack(idx + 1, curr, curr_s + candidates[idx])

            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            
            curr.pop()
            backtrack(idx + 1, curr, curr_s)
        
        backtrack(0, [], 0)
        return res


            