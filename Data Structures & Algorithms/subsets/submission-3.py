class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtracking(idx, curr):

            if idx >= len(nums):
                res.append(curr[::])
                return
            
            curr.append(nums[idx])
            backtracking(idx + 1, curr)
            curr.pop()
            backtracking(idx + 1, curr)
        
        backtracking(0, [])
        return res