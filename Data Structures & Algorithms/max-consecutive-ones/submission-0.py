class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        res = 0
        for n in nums:
            
            if n == 1:
                count += 1
            if n == 0:
                count = 0
            res = max(res, count)
        
        return res