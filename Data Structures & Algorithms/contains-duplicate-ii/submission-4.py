class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict_nums = {}

        for i, n in enumerate(nums):
            if n in dict_nums and abs(dict_nums[n] - i) <= k:
                return True

            dict_nums[n] = i
        
        return False
