# Session 1, attempt 1: Top Down
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHelper(i, memo={}):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]
            
            #check options
            # either steal from this house or not.
            res = max(robHelper(i-2) + nums[i], robHelper(i-1))

            memo[i] = res
            return res
        
        return robHelper(len(nums)-1)