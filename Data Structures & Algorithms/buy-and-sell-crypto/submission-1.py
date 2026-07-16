class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        buy = prices[0]
        for price in prices[1:]:
            buy = min(buy, price)
            mp = max(mp, price-buy)
        return mp