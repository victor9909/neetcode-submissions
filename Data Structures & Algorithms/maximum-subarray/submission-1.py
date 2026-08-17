class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = 0
        maxsum = nums[0]

        for n in nums:
            curr = max(n, curr + n)
            maxsum = max(curr, maxsum)
        
        return maxsum