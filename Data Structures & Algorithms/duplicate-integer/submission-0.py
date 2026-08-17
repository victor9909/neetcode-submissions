class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        set_nums = set()
        for n in nums:
            if n in set_nums:
                return True
            set_nums.add(n)
        
        return False