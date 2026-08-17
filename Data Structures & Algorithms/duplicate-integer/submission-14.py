class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dict_nums = Counter(nums)
        for k in dict_nums:
            if dict_nums[k] >= 2:
                return True
        return False