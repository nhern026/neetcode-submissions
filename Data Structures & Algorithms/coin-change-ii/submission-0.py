class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amt = amount
        dp = []
        for x in range(amt+1):
            row = []
            for y in range(len(coins)+1):
                row.append(0)
            dp.append(row)
            
        
        for c in range(len(coins)):
            dp[0][c] = 1
        
        
        for tgt in range(1, amt+1):
            for idx in range(len(coins) - 1, -1, -1):
                use_coin_cominations = 0
                if tgt - coins[idx] >= 0:
                    use_coin_cominations = dp[tgt - coins[idx]][idx]
                    
                skip_coin_combinations = dp[tgt][idx+1] # always true because idx never is rightmost col
                    
                dp[tgt][idx] = use_coin_cominations + skip_coin_combinations
        
        return dp[amt][0]