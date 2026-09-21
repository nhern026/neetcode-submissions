# Session 1, attempt 1: 
    # had an issue when the last number is included in the subTotal --> reordered the base case statements to check i == len(candidates) after if count == target
    # cheeky duplicate reduction by skipping values when we DON"T choose that number.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        subTotal = []
        def dfs(i, count):
            if count == target:
                res.append(subTotal.copy())
                return
            if count > target or i == len(candidates):
                return
        
            # we add this number
            subTotal.append(candidates[i])
            dfs(i+1, count+candidates[i])

            # we don't choose that number, and skip any number that is the same
            subTotal.pop()
            new_idx = i + 1
            while new_idx < len(candidates) and candidates[new_idx-1] == candidates[new_idx]:
                new_idx += 1
            if new_idx == len(candidates):
                return
            dfs(new_idx, count)


        dfs(0, 0)
        return res