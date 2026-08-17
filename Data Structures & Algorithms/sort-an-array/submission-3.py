class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        min_n = min(nums) if min(nums) >= 0 else min(nums)* -1
        nums_c = [min_n + n for n in nums]

        dict_nums = {}
        max_n = max(nums_c)
        for i in range(max_n + 1):
            dict_nums[i] = 0
        
        for n in nums_c:
            dict_nums[n] += 1
        
        res = []
        for i in range(max_n + 1):
            occ = dict_nums[i]
            for _ in range(occ):
                res.append(i - min_n)
        return res
