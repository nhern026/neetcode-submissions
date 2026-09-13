#session 1, second attempt. after reading hint this is much better. 
    #just really jank code lol.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findStartingidx():
            #find the edge:
            left = 0
            right = len(nums) - 1

            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]: #middle is in LARGER NUMS
                    left = mid + 1
                else:
                    right = mid

            #we have starting index. so now we can get sexy
            return left

        startingIdx = findStartingidx()
        print(startingIdx)

        if nums[startingIdx] <= target and target <= nums[-1]:
            left, right = startingIdx, len(nums)-1
        elif nums[startingIdx-1] >= target and target >= nums[0]:
            left, right = 0, startingIdx-1
        else:
            return -1

        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
            
