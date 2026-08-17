class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(curr, i):

            if i == len(nums):
                res.append(curr[::])
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                curr.append(nums[i])
                backtrack(curr, i + 1)
                nums[i], nums[j] = nums[j], nums[i]
                curr.pop()
        
        backtrack([], 0)
        return res