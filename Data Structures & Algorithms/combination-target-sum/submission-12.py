# Session 2, attempt 1
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subtotal = []
        def dfs(i, count):
            if count > target or i == len(nums):
                return
            if count == target:
                res.append(subtotal.copy())
                return

            
            subtotal.append(nums[i])
            count += nums[i]
            dfs(i, count) 

            subtotal.pop()
            count -= nums[i]
            dfs(i+1, count)

        dfs(0, 0)
        return res