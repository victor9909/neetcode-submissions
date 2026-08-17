class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def dfs(idx, curr, curr_sum):

            if curr_sum == target:
                res.append(curr[::])
                return
            if idx >= len(nums) or curr_sum > target:
                return
            
            curr.append(nums[idx])
            dfs(idx, curr, curr_sum + nums[idx])
            curr.pop()
            dfs(idx + 1, curr, curr_sum)
        
        dfs(0, [], 0)
        return res


