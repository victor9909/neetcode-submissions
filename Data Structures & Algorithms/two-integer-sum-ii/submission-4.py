class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dict_nums = {}
        for idx, n in enumerate(numbers):
            find = target - n
            if find in dict_nums:
                return [dict_nums[find] + 1, idx + 1]
            dict_nums[n] = idx
            