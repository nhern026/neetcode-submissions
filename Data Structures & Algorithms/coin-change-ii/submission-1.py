class Solution: # unbounded knapsack
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        # coins = [1,2,3]   
        # dp = [1, 0, 0, 0, 0]
        #       0, 1, 2, 3, 4 <-- state val is the index

        # after one pass:
        # dp = [1, 1, 1, 1, 1]

        # after second pass:
        # dp = [1, 1, 2, 2, 3]

        # after third pass:
        # dp = [1, 1, 2, 3, 4]

        for c in coins:
            for state_val in range(c, amount + 1):
                dp[state_val] += dp[state_val - c]

        return dp[-1]
