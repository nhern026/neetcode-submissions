# Session 1, attempt1: neetcode video, i kinda also thought this would be best way to do it, but i'm using his two variable solution instead of making a whole dp array

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHelper(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                newRob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2
        
        if len(nums) == 1:
            return nums[0]
        else:
            return max(robHelper(nums[1:]), robHelper(nums[:-1]))