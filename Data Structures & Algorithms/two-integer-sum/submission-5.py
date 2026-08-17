class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_nums = {}
        for i, n in enumerate(nums):
            check = target - n
            if check in dict_nums:
                return [dict_nums[check], i]
            dict_nums[n] = i
