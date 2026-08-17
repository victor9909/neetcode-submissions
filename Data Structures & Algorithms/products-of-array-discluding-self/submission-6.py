class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * (len(nums) + 1)
        curr = 1
        for i in range(0, len(nums)):
            curr *= nums[i]
            prefix[i + 1] *= curr
        
        postfix = [1] * (len(nums) + 1)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            curr *= nums[i]
            postfix[len(nums) - i] *= curr
        
        res = []
        postfix = postfix[::-1]

        for i in range(len(nums)):
            right = postfix[i + 1] 
            left = prefix[i]
            res.append(right * left)
        return res
