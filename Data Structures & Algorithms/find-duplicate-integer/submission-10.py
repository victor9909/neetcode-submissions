class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        s, f = nums[0], nums[0]
        while True:
            s, f = nums[s], nums[nums[f]]
            if s == f:
                break
        
        s1 = nums[0]
        while True:
            if s == s1:
                return s
            s, s1 = nums[s], nums[s1]
        