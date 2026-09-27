# Session 1, attempt 1: watched neetcode and greg hogg's videos.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        curr_sum = 0

        for n in nums:
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
            if curr_sum <= 0: # should ask if we want 0's or not
                curr_sum = 0
        
        return max_sum
