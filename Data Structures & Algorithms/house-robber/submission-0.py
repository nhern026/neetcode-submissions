# Session 1, attempt 2: first attempt at Bottom Up
class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-math.inf] * len(nums)
        dp[0] = nums[0]

        if len(nums) > 1:
            dp[1] = nums[1]

        max_prev = dp[0]

        for i in range(2, len(nums)):
            dp[i] = nums[i] + max_prev
            max_prev = max(dp[i-1], max_prev)
            

        return max(dp)