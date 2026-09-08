class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = nums[0]
        votes = 0

        for n in nums:
            if candidate == n:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    candidate = n
                    votes = 1
        return candidate
