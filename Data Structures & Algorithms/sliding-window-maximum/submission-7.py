class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # [1,2,1,0,4,2,6] k = 3
        # [1, 2] -> 2
        # [1,2,3] -> 2
        # [4] -> 4
        # [4, 5] -> 4
        # [6] -> 6

        q = deque()
        l = 0
        res = []
        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
        return res
            
            
            
