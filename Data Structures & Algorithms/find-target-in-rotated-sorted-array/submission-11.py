class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(left, right, target):
            while left <= right:
                mid = (right + left) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            
            return -1





        
        def findSplitID(nums):
            left, right = 0, len(nums)-1

            while left < right:
                mid = (right + left) // 2

                if nums[mid] < nums[right]:
                    right = mid
                elif nums[mid] > nums[right]:
                    left = mid + 1
            
            return left
        
        startID = findSplitID(nums)
        if nums[startID] <= target <= nums[len(nums)-1]: # if in right side
            return bst(startID, len(nums)-1, target)
        elif startID != 0 and (nums[0] <= target <= nums[startID - 1]): # if in left side
            return bst(0, startID - 1, target)
        else:
            return -1



