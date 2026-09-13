# Session 1, attempt 2
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) #have to add copy
                return
            
            # left decision, to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res