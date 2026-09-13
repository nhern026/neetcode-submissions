# Session 3, attempt 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy, sell = 0, 0, 1


        while buy < len(prices) and sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1

        return profit

    # [7,1,5,3,6,4]
    # b s
    # 7 1
    # 
        