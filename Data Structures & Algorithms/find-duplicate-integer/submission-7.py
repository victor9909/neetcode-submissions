class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = nums[0], nums[nums[0]]
        while True:
            if slow == fast:
                break
            slow, fast = nums[slow], nums[nums[fast]]
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

