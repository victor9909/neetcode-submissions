class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dict_set = set()
        for idx, n in enumerate(nums):
            if n in dict_set:
                return True
            dict_set.add(n)
        return False
