class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if (right - left) <= 1: #the only situation where min is nums[left] is when it was rotated n times. i think
                return min(nums[right], nums[left])
            
            mid = (left + right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1 #you can do +1 because in this situation you already know right is less than mid (since all numbers are unique and nums[right] is not bigger than nums[mid]), so you can confidently skip checkign mid again. in the other example, all we know is that the middle numbers ie less than right. so that middle number could possibly be our minimum. 
            
            #you can also do this by comparing nums[left] instead of nums[right]. doing that you're essentially asking if nums[m] >= nums[l] (am i in left [greater] portion of sorted array)
        
