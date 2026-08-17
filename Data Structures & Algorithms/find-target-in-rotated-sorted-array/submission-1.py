class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # [3,4,5,6,1,2] 1
        # l = 0, r = 5 m = 2 -> nums[m] == 1 ? Nope
        # l = 0, r = 5 target < nums[l] -> l = m + 1 -> 3
        # l = 3, r = 5 

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            else:
                if nums[l] <= nums[m]:
                    if nums[l] > target or nums[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if target < nums[m] or nums[r] < target:
                        r = m - 1
                    else:
                        l = m + 1
        
        return -1

