# Session 2, attempt 1

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # okay so we need some monotonic stack it seems like since we're holding max

        # okay great so at each window we should know the max (first element on our stack)
        # and then the possible future max's after

        #[1  2  1] 0  0 4  2  6        because when we look at this here. 2 is our max now, but 1 will be later
        #1  [2  1  0]  0 4  2  6   still 2 here but 1 could be later, and then 0 could be later too!
        #1  2  [1  0  0] 4  2  6    see now 1 is our max! and so could 0 or 0 be as well later
        #1  2  1  [0  0  4]  2  6  well here 4 is our max and no other number in this window could ver be max again. right so we can trace that behaveior with a monotonic stack:


        # for each new element we check if the top element in our stack is smaller, if it is we pop.
        # we keep doing that until either our stack is empty or the top value is bigger.
        # then we append that val.
        # our max is for the window will always be at the bottom of the stack
        # FINALLY, once we shift the window over, l += 1, if that element at pos l is our current max, then we popleft from our stack. 

        # cool lets do it

        # build first window:
        l, r = 0, 0
        max_holder = deque()
        while r < k:
            while max_holder and max_holder[-1] < nums[r]:
                max_holder.pop()
            
            max_holder.append(nums[r])

            r+= 1

        
        r -= 1

        # now we are at l = 0, and r = k-1 and a valid max_holder

        res = []
        while r < len(nums):
            res.append(max_holder[0])
            
            # if we are losing our max, get rid of it
            if nums[l] == max_holder[0]:
                max_holder.popleft()
            
            # expanding and adding new number
            if r < len(nums)-1:
                while max_holder and max_holder[-1] < nums[r+1]:
                    max_holder.pop()
                max_holder.append(nums[r+1])

            l += 1
            r += 1

        return res
                






