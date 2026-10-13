# Session 3, attempt 1: items outer, capacity inner
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = [1,5,10], amount = 12

        dp = []
        for _ in range(amount+1):
            dp.append(math.inf)
        dp[0] = 0

        #dp = [0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

        # after first pass:
        #dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # after second pass:
        #dp = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4]

        # after third pass:
        #dp = [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3]


        for c in coins:
            for state_val in range(c, amount+1): 
                dp[state_val] = min(dp[state_val], dp[state_val - c] + 1) 
        
        return dp[-1] if dp[-1] < math.inf else -1
        
        