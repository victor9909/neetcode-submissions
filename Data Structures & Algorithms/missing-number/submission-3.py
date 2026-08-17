class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        max_range = len(nums)
        xor_r = 0
        for n in range(max_range + 1):
            xor_r ^= n
        
        for n in nums:
            xor_r ^=n

        return xor_r