class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
       # nums = [1,2,4,6]
       # [1,2,4,6]
       # [1 2 8 48]
       # [48 48 24 6] 

       # [48 24 12 8]

        prefix = []
        curr = 1
        for n in nums:
            curr *= n
            prefix.append(curr)
        
        postfix = []
        curr = 1
        for n in nums[::-1]:
            curr *= n
            postfix.append(curr)
        
        res = []
        for i,n in enumerate(nums):
            pre = prefix[i-1] if i-1 >= 0 else 1
            post = postfix[::-1][i+1] if i+1 < len(nums) else 1
            res.append(pre * post)
        
        return res


        

    

        