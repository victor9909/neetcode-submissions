class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def backtrack(i):

            if i >= len(nums):
                res.append(nums[::])
                return
            
            used = set()

            for j in range(i, len(nums)):
                if nums[j] in used:
                    continue
                used.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        
        backtrack(0)
        return res