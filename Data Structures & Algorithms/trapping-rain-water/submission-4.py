class Solution:
    def trap(self, height: List[int]) -> int:
        
        # [0,2,0,3,1,0,1,3,2,1]
        #  0 2 2 3 3 3 3 3 3 3
        #  3 3 3 3 3 3 3 3 2 1

        #  0 0 2 0 2 3 2 0 0 0 -> 9

        prefix = []
        curr = 0
        for h in height:
            curr = max(curr, h)
            prefix.append(curr)
        
        postfix = []
        curr = 0
        for h in height[::-1]:
            curr = max(curr, h)
            postfix.append(curr)
        postfix = postfix[::-1]

        res = 0
        for i in range(len(height)):
            res += min(prefix[i], postfix[i]) - height[i]
        return res
