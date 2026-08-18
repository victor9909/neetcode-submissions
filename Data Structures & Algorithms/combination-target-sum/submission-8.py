class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, curr, curr_s):
            
            if curr_s == target:
                res.append(curr[::])
                return

            if i >= len(nums) or curr_s > target:
                return
            
            curr.append(nums[i])
            backtrack(i, curr, curr_s + nums[i])
            curr.pop()
            backtrack(i + 1, curr, curr_s)
        
        backtrack(0, [], 0)
        return res