class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        buy = prices[0]
        sell = 0
        for price in prices:
            sell = max(sell,price)
            if price<buy:
                buy = price
                sell = price
            mp = max(mp, sell-buy)
        return mp