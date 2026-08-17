class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = []
        def backtrack(curr, i):
            if i == len(nums):
                res.append(curr)
                return
            
            curr ^= nums[i]
            backtrack(curr, i + 1)
            curr ^= nums[i]
            backtrack(curr, i + 1)
        
        backtrack(0, 0)
        return sum(res)