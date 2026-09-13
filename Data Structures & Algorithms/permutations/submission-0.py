class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, permutation = [],[]

        def backtrack():
            if len(permutation) == n:
                res.append(permutation.copy())
                return
            
            for x in nums:
                if x not in permutation:
                    permutation.append(x)
                    backtrack()
                    permutation.pop()
        
        backtrack()
        return res