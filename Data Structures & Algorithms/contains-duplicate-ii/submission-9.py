class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict_nums = defaultdict(list)
        for i, n in enumerate(nums):
            dict_nums[n].append(i)
            indexes = dict_nums[n]
            if len(indexes) >= 2 and abs(indexes[-1] - indexes[-2]) <= k:
                return True
            
        return False
