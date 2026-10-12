# Session 2, attempt 2: getting rid of first loop

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_holder = deque()
        res = []

        l, r = -k+1, 0
        while r < len(nums):
            # expanding and adding new number
            if r < len(nums):
                while max_holder and max_holder[-1] < nums[r]:
                    max_holder.pop()
                max_holder.append(nums[r])
            
            # start recording once l is >= 0
            if l >= 0:
                res.append(max_holder[0])
            
                # if we are losing our max, get rid of it
                if nums[l] == max_holder[0]:
                    max_holder.popleft()
                    
            l += 1
            r += 1

        return res








