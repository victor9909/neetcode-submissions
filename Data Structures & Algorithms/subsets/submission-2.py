class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(idx):

            if idx == len(nums):
                res.append(subset[::])
                return
            
            # Decision to add
            subset.append(nums[idx])
            dfs(idx + 1)

            # Decision not to add
            subset.pop()
            dfs(idx + 1)
        
        dfs(0)
        return res

            
            
            

            