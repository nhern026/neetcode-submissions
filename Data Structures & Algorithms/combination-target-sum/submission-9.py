# Session 1, attempt 3: neetcode video

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # cur is current combination
        # total is sum of current combination
        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:]) #[:] is a shallow copy
                return
            if i >= len(nums) or total > target:
                return
            
            # first decision
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            
            # second decision
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res



