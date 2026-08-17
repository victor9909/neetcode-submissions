class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i):

            # Base Case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Left decision of tree to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Right decision of tree to NOT include nums[i]
            subset.pop()
            dfs(i + 1)
    
        dfs(0)
        return res