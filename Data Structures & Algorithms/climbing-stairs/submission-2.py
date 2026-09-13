# Session 1, attempt 1: neetcode's bottom up approach but with O(n) space
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]

        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
            print(dp[i-1], " + ", dp[i-2], " = ", dp[i])
        
        return dp[n]
        
        