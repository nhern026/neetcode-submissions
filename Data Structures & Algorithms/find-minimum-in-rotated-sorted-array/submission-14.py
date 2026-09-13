class Solution:
    #this version stops when left == right. makes it cleaner and ensures the min is at the left. the last version also the min has to be on the left BUT because it stops when left is adjacent to right you can't ensure which is the min. but if you let it update one more time and allow left and right to point to the same thing, it'll break the while loop and you only have to return nums[left] or nums[right]. essentially the same this one just might be a little cleaner. 

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:            
            mid = (left + right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1  
        return nums[left]
        
