# Session 1, attempt 2: neetcode video
# after watching 6:14 of neetcode video

# its stupid easy whenyou think of it like the way he said
# i like to thinka bout it like this: 
# each spot is a hill
# if you are on the hill, look left and see the tallest peak behind you
# look right and see the tallest peak ahead of you
# if it rained, would your hill be submerged in water
        # in between two taller peaks?,yes! how much? by the smallest peak - your hill's height
        # otherwise if you're not in between two taller peaks, well you woudln't be submerged!

class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = []
        maxR = [0] * len(height)

        prev = 0
        for num in height:
            prev = max(prev, num)
            maxL.append(prev)
        
        post = 0
        for i in range(len(height)-1, -1, -1):
            post = max(post, height[i])
            maxR[i] = post

        res = [0] * len(height)

        for i in range(len(height)):
            water_area = min(maxL[i], maxR[i]) - height[i]
            res[i] = max(res[i], water_area)

        return sum(res)