class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res = []

        def backtrack(i, curr):

            if i >= len(nums):
                res.append(curr)
                return
            
            backtrack(i + 1, curr ^ nums[i])
            backtrack(i + 1, curr)
        
        backtrack(0, 0)
        return sum(res)