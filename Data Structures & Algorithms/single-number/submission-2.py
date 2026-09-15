class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        curr = 0
        for n in nums:
            curr ^= n
        return curr