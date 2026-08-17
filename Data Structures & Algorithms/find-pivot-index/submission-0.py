class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix = []
        tot = 0
        for n in nums:
            tot += n
            prefix.append(tot)
        
        postfix = []
        tot = 0
        for n in nums[::-1]:
            tot += n
            postfix.append(tot)
        postfix = postfix[::-1]
        
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        return -1
        
