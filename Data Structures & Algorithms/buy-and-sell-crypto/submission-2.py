# Session 2, attempt 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        bestProfit = 0

        for price in prices:
            if price < buy: 
                buy = price
            else:
                profit = price - buy
                bestProfit = max(bestProfit, profit)

        return bestProfit
            
        