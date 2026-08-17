class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums) # for O(1) lookup
        res = 0

        for n in nums:
            # Potential start interval
            if n - 1 not in nums_set:
                lenght = 0
                while n + lenght in nums_set:
                    lenght += 1
                res = max(res, lenght)
        return res

