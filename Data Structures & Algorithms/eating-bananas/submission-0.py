class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # piles = [1,4,3,2], h = 9
        # [1, 2, 3, 4] l= 0, r = 3 -> m = 1 k = 2
        # 1, 1, 2, 2 -> 6
        # 1, 2, 3, 4 -> 10

        l, r = 1, max(piles)
        res = 0
        while l <= r:
            k = (l + r) // 2
            target = 0
            for p in piles:
                target += math.ceil(p/k)
            
            if target <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res
