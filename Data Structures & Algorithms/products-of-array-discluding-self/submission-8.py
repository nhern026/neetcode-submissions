# Session 2, attempt 2: trying in two passes
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        pre = 1
        post = 1

        for i in range(len(nums)):
            res[i] = pre 
            pre = pre * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]

        return res
