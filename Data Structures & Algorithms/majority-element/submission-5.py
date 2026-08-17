class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        votes = 0
        candidate = nums[0]

        for n in nums:
            if n == candidate:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    votes = 1
                    candidate = n
        
        return candidate