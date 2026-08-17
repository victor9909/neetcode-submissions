class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        if len(nums) == 1:
            return [nums[:]] # nums.copy() is weight
        
        for i in range(len(nums)):
            n = nums.pop() # [1, 2, 3] exlude the first element
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            
            result.extend(perms)
            nums.append(n) # We will have [2, 3, 1] for next cycle

        return result
