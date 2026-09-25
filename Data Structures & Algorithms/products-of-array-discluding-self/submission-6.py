# Session 2, attempt 1: after learning prefix and postfix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []

        prev = 1
        for n in nums:
            prefix.append(prev * n)
            prev = prev * n

        postfix = [0] * len(nums)
        prev = 1
        for idx in range(len(nums)-1, -1, -1):
            postfix[idx] = prev * nums[idx]
            prev = prev * nums[idx]

        res = [0] * len(nums)
        for i in range(len(res)):
            if i == 0:
                pre = 1
            else:
                pre = prefix[i-1]

            if i == len(res) - 1:
                post = 1
            else:
                post = postfix[i+1]
            
            res[i] = pre * post

        # print(prefix)
        # print(postfix)
        return res
