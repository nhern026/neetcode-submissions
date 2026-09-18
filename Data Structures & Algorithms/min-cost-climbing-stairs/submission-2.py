# Session 1, attempt 2: top down approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def topDown(i, memo = {}):
            if i == 0 or i == 1:
                return 0
            if i in memo:
                return memo[i]

            stair_cost = min(topDown(i-2) + cost[i-2], topDown(i-1) + cost[i-1])
            memo[i] = stair_cost
            return stair_cost
        
        return topDown(len(cost))