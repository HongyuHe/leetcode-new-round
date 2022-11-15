class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                # * Buy > Sell
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        #> l==r
        return max_profit