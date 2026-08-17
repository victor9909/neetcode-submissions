class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_n = {}
        for idx, n in enumerate(nums):
            find = target - n
            if find in dict_n:
                return [dict_n[find], idx]
            dict_n[n] = idx