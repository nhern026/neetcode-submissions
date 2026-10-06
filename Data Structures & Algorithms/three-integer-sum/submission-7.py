# Session 3, attempt 1:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for first in range(len(nums)-2):
            if first > 0 and nums[first-1] == nums[first]:
                continue

            tgt = -nums[first]

            second = first+1
            third = len(nums)-1

            while second < third:
                if nums[second] + nums[third] == tgt:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                elif nums[second] + nums[third] < tgt:
                    second += 1
                else:
                    third -= 1
                
                while second < len(nums) and second > first + 1 and nums[second] == nums[second-1]: #if not first idx and equal to the last one
                    second += 1
                while third > second and third < len(nums)-1 and nums[third] == nums[third+1]:
                    third -= 1
                
        return res

 


