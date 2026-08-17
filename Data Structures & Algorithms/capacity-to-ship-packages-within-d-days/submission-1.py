class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l, r = max(weights), sum(weights)

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

        res = 0
        while l <= r:
            capacity = (l + r) // 2

            if sufficient_cap(capacity):
                r = capacity - 1
                res = capacity
            else:
                l = capacity + 1
        
        return res
        






