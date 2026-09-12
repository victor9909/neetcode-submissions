class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 1  2   4  6
        # 1  1  2   8  48
        # 48 48  24  6 1

        # 48 24 12 8

        prefix = [1]
        curr = 1
        for i in range(len(nums)):
            prefix.append(curr * nums[i])
            curr *= nums[i]
        
        postfix = [1]
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix.append(curr * nums[i])
            curr *= nums[i]
        postfix = postfix[::-1]
        
        res = []
        
        for i in range(1, len(nums) + 1):
            res.append(prefix[i - 1] * postfix[i])
        return res
