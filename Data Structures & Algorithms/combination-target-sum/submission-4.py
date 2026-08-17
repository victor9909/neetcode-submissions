class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(idx, curr, curr_s):

            if curr_s > target or idx >= len(nums):
                return
            
            if curr_s == target:
                res.append(curr[::])
                return
            
            curr.append(nums[idx])
            backtrack(idx, curr, curr_s + nums[idx])
            curr.pop()
            backtrack(idx + 1, curr, curr_s)
        
        backtrack(0, [], 0)
        return res