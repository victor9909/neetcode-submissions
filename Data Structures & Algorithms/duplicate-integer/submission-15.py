class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Time O(N)
        # Space O(N)
        
        nums_set = set()
        for n in nums:
            if n in nums_set:
                return True
            nums_set.add(n)
        return False