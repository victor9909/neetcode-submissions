class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict_nums = {}

        for i, n in enumerate(nums):
            if n not in dict_nums:
                dict_nums[n] = i
            else:
                idx = dict_nums[n]
                if abs(idx - i) <= k:
                    return True
                dict_nums[n] = i
        return False

        
