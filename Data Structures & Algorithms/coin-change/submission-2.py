# Session 3, attempt 1: 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = [1,5,10], amount = 12

        dp = []
        for _ in range(amount+1):
            dp.append(math.inf)
        #dp = [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

        # setting base cases
        for c in coins:
            if c <= amount:
                dp[c] = 1
        dp[0] = 0
        #dp = [0, 1, inf, inf, inf, 1, inf, inf, inf, inf, 1, inf, inf]

        for state_val in range(1, amount+1):
            min_amount_needed = dp[state_val]
            if min_amount_needed == 1:
                continue
                
            for c in coins:
                if state_val - c >= 0:
                    min_amount_needed = min(min_amount_needed, dp[state_val - c])
            
            dp[state_val] = min_amount_needed + 1

        
        return dp[-1] if dp[-1] < math.inf else -1

        """
        amount = 0 --> works dp=[0]

        coins = [1, 5, 10]
              0. 1. 2. 3.  4.  5. 6.  7.  8.   9.  10. 11.  12
        dp = [0, 1, 2, 3,  4,  1, 2,  3,  , inf, 1, inf, inf]
        min = min(inf, 1)



        """







        
        