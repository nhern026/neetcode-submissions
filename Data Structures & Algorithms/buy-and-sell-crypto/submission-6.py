# Session 3, attempt 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy, sell = 0, 0, 1

        while sell < len(prices): # could only do sell < ... but this is more clear
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1 # i can take them out and put sell+=1 under while loop but this is more clear
            else:
                profit = max(profit, prices[sell] - prices[buy])
                sell += 1

        return profit

    # [7,1,5,3,6,4]
    # b s
    # 7 1, no profit check
    # 1, 5, 4
    # 1, 3 4
    # 1, 6 5
    # 1, 4 5
    # end
        