# Session 1, attempt 1
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            l, r = 0, 0 # window of size 3 starts off at -2:1
    
            res = []
            q = deque()
            while r < k:
                while q and nums[r] > q[-1]:
                    q.pop()
                q.append(nums[r])
                r+= 1

            r -= 1
            while r < len(nums):
                # print(l, r)
                # print(q)
                # print()
                res.append(q[0])

                l += 1
                if nums[l-1] == q[0]: # if we are removing the max
                    q.popleft()
                # else it doesnt' matter

                r += 1
                if r < len(nums): # if we haven't reached the end
                    while q and nums[r] > q[-1]: # keep popping from right until nums[r] is right of something bigger than it or nothing
                        q.pop()
                    q.append(nums[r])

                else:
                    continue
        
            return res

