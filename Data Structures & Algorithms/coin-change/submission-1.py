# Sessoin 2, attempt 1: 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount+1) # we'll use the index of the dp to be the state (target amount left)
        dp[0] = 0 # if the target amount is zero




        for c in coins: # if the target amount is a coin
            if c <= amount:
                dp[c] = 1
        
        # coins = [2, 3]   amount = 5
        # dp = [0, inf, 1, 1, inf, inf]

        # i = 1
        # dp = [0, inf, 1, 1, inf, inf]

        # i = 2, gets skipped
        # i = 3, gets skipped

        # i = 4
        # dp = [0, inf, 1, 1, min(1, inf) + 1, inf]

        # i = 5
        # dp = [0, inf, 1, 1, 2, min(1, 1)+1]

        # return dp[5] which is 2!

        # coins = [5] , amount = 3
        # dp = [0, inf, inf, inf, min(1, inf) + 1, inf]

        for i in range(1, amount+1):
            min_amount_needed = dp[i]
            for c in coins:
                if i - c >= 0:
                    min_amount_needed = min(min_amount_needed, dp[i-c])
            
            dp[i] = min_amount_needed + 1 

        return dp[amount] if dp[amount] < math.inf else -1