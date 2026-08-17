class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        visit = set()

        for r in range(len(nums)):
            if abs(r - l) > k:
                visit.remove(nums[l])
                l += 1 
            if nums[r] in visit:
                return True
            visit.add(nums[r])

        return False