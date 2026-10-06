# Session 3, attempt 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findSplit(l, r):
            while l != r: 
                mid = (l + r) // 2

                if nums[mid] < nums[r]:
                    r = mid
                else: #nums[mid] > nums[r]
                    l = mid + 1            
            return l

        def bs_search(l, r):
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return -1


        split_idx = findSplit(0, len(nums)-1)

        if target > nums[len(nums)-1]:
            start = 0
            end = split_idx - 1
        else:
            start = split_idx
            end = len(nums)-1
            
        return bs_search(start, end)