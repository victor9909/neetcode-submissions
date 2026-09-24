class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l, r = max(nums), sum(nums)
        res = 0

        def check_k(candidate):
            
            curr_s = 0
            partitions = 0
            for n in nums:
                if curr_s + n > candidate:
                    partitions += 1
                    curr_s = n
                else:
                    curr_s += n

            return partitions + 1 <= k


        while l <= r:
            m = l + (r - l) // 2

            if check_k(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res

