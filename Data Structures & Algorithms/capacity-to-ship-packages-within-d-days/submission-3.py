class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        # [2,4,6,1,3,10] days = 4
        # [1,2,3,4,6,10]
        # l = 10 r = 26 m = 18

        # l = 10 r = 17 m = 13
        # l = 10 r = 12 m = 11
        # l = 10 r = 10 m = 10

        l, r = max(weights), sum(weights)
        res = None

        def sufficient_cap(cap):

            curr_w = 0
            curr_d = 1

            for w in weights:
                if curr_w + w <= cap:
                    curr_w += w
                elif curr_w + w > cap:
                    curr_w = w
                    curr_d += 1
            return curr_d <= days

        while l <= r:
            m = l + (r - l) // 2
            if sufficient_cap(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res




