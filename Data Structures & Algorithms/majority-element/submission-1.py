class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        min_num = math.ceil(len(nums) / 2)
        dict_nums = {}
        for n in nums:
            dict_nums[n] = dict_nums.get(n, 0) + 1
            if dict_nums[n] >= min_num:
                return n
        