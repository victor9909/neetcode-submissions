class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums.sort()
        res = []

        for idx, n in enumerate(nums):
            # Salto i duplicati
            if idx > 0 and nums[idx - 1] == n:
                continue
            
            l, r = idx + 1, len(nums) - 1

            while l < r:
                curr_sum = n + nums[l] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    res.append((n, nums[l], nums[r]))
                    l += 1
                    while l < len(nums) - 1 and nums[l - 1] == nums[l]:
                        l += 1
        
        return res
