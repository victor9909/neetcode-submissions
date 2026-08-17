class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        def backtracking(idx, curr):

            res.append(curr[::])

            for j in range(idx, len(nums)):
                if j > idx and nums[j] == nums[j - 1]:
                    continue
                curr.append(nums[j])
                backtracking(j+1, curr)
                curr.pop()
        
        backtracking(0, [])
        return res