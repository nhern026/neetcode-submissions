# Session 2, attempt 1
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = []
        memo.append(1)
        memo.append(1)
        
        for i in range(2, n+1): #
            memo.append(memo[i-2] + memo[i-1])

    
        return memo[n]