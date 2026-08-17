class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        max_l = 0

        for n in nums:
            if n-1 not in nums_set:
                leng = 0
                while n + leng in nums_set:
                    leng += 1
                max_l = max(leng, max_l)
        
        return max_l
