class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(curr, curr_s, i):
            nonlocal target
            if curr_s == target:
                res.append(curr[::])
                return
            
            if curr_s > target or i == len(nums):
                return
            
            curr.append(nums[i])
            backtrack(curr, curr_s + nums[i], i)
            curr.pop()
            backtrack(curr, curr_s, i + 1)
        
        backtrack([], 0, 0)
        return res