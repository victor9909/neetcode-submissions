class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l, r = max(nums), sum(nums)

        def split_arr(tmp):

            curr_s = 0
            res = 1
            for n in nums:
                if curr_s + n <= tmp:
                    curr_s += n
                elif curr_s + n > tmp:
                    curr_s = n
                    res += 1
            
            return res <= k
        
        res = 0
        while l <= r:
            m = (l + r) // 2

            if split_arr(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res