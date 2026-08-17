class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()


        def backtracking(curr, curr_sum, idx):

            if target == curr_sum:
                res.append(curr[::])
                return
            
            if idx >= len(candidates) or target < curr_sum:
                return
            
            curr.append(candidates[idx])
            backtracking(curr, curr_sum + candidates[idx], idx + 1)
            curr.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            backtracking(curr, curr_sum, idx + 1)

        backtracking([], 0, 0)
        return res
