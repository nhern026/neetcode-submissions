# Session 1, attempt 1:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 0
        isZero = False

        for i in range(len(nums)):
            if nums[i] != 0:
                if not prod:
                    prod = 1
                prod *= nums[i]
            else:
                if isZero:
                    prod = 0
                    break
                isZero = True
        
        res = []
        for x in nums:
            if x != 0:
                if not isZero:
                    res.append(prod//x)
                else:
                    res.append(0)
            else:
                res.append(prod)

        return res