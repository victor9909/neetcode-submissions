class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(idx, curr, cur_sum):

            if idx >= len(nums) or cur_sum > target:
                return
            
            if cur_sum == target:
                res.append(curr[::])
                return
            
            curr.append(nums[idx])
            backtrack(idx, curr, cur_sum + nums[idx])
            curr.pop()
            backtrack(idx + 1, curr, cur_sum)
        
        backtrack(0, [], 0)
        return res