# Session 2, attempt 2: getting rid of first loop

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

        """
        [1, 3, -1, -3, 5, 3, 6, 7] -->  res=[3, 3, 5, 5, 6, 7]
        


        """








