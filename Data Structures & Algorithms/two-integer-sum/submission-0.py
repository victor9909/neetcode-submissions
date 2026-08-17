class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        dict_nums = {}
        for i, n in enumerate(nums):
            to_find = target - n
            if to_find in dict_nums:
                return [dict_nums[to_find], i]
            dict_nums[n] = i