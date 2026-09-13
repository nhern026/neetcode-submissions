class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            bestProfit = max(price - buy, bestProfit)

        return bestProfit