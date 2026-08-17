class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, curr_s, curr):

            if curr_s == target:
                res.append(curr[::])
                return
            
            if curr_s > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            backtrack(i, curr_s + nums[i], curr)
            curr.pop()
            backtrack(i + 1, curr_s, curr)
        
        backtrack(0, 0, [])
        return res
