class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 0
        res = 0

        while r < len(prices):
            if prices[r] >= prices[l]:
                res = max(prices[r] - prices[l], res)
                r += 1
            else:
                l += 1
        return res