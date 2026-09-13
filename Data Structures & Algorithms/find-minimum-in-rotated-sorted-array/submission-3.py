class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if (right - left) <= 1:
                return min(nums[right], nums[left])
            
            mid = (left + right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
            
        
