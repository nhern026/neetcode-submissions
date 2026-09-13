class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bestArea = 0
        left, right = 0, (len(heights) - 1)

        while left < right:
            # calculating and udpating our max area 
            currArea = (right - left) * min(heights[left], heights[right])
            bestArea = max(bestArea, currArea)

            # moving the pointer with the smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return bestArea

