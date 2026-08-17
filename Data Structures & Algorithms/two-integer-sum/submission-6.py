class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_nums = {}
        for i, n in enumerate(nums):
            find = target - n
            if find in dict_nums:
                return [dict_nums[find], i]
            dict_nums[n] = i