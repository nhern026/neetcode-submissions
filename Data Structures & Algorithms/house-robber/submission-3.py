# Session 1, attempt 1: Bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-math.inf] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1]) 

        for i in range(2, len(nums)):
            # dp[i] = max between stealing from here OR skipping house
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]


