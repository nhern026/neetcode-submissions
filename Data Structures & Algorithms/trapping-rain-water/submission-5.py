class Solution:
    def trap(self, height: List[int]) -> int:
        peak_left = [0] * len(height)

        peak_right = [0] * len(height)

        max_height = 0
        for idx in range(len(height)):
            peak_left[idx] = max(max_height, height[idx])
            max_height = peak_left[idx]
        
        max_height = 0
        for idx in range(len(height)-1, -1, -1):
            peak_right[idx] = max(max_height, height[idx])
            max_height = peak_right[idx]

        wtr_area = 0
        for i in range(len(height)):
            wtr_area += min(peak_left[i], peak_right[i]) - height[i]

        return wtr_area


        