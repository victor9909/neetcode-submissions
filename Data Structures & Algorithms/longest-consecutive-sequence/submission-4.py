class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_s = set(nums)
        res = 0

        for n in nums_s:
            if n - 1 not in nums_s:
                length = 0
                while n + length in nums_s:
                    length += 1
                res = max(res, length)
        return res