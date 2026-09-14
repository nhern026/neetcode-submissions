# Session 2, attempt 1
class Solution:
    def climbStairs(self, n: int) -> int:
        bottomUp = []
        bottomUp.append(1)
        bottomUp.append(1)
        
        for i in range(2, n+1): #
            bottomUp.append(bottomUp[i-2] + bottomUp[i-1])

    
        return bottomUp[n]