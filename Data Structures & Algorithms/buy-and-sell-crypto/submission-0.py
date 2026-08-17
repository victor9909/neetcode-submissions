class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # prices = [10,1,5,6,7,1]
        # l = 0, r = 1 -> l < r ? Nope
        # l = 1, r = 2 -> l < r ? 4
        # l = 1 r = 3 -> l < r ? 5
        # l = 1 r = 4 -> l < r ? 6
        # l = 1 r = 5 -> l < r ? 1 -> 6

        res = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] <= prices[r]:
                res = max(res, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1

        return res
        