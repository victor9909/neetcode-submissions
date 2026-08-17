class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or len(nums) <= i:
                return
            
            # Decision to add nums[i]
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # Decision to not include nums[i]
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res