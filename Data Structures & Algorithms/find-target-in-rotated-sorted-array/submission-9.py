#session 1, first attempt. Funky BST, too much work lol. 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #old index finder
        def oldIdx(idx):
            if idx >= len(nums):
                idx -= len(nums)
            return idx

        #new index finder
        def newIdx(idx, start):
            if idx < start:
                idx += len(nums)
            return idx


        def findStartingidx():
            #find the edge:
            left = 0
            right = len(nums) - 1

            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]: #middle is in LARGER NUMS
                    left = mid + 1
                else:
                    right = mid

            #we have starting index. so now we can get sexy
            return left
        

        startingIdx = findStartingidx()

        #then we do a funky BST
        left = newIdx(startingIdx, startingIdx)
        right = newIdx(startingIdx - 1, startingIdx)

        while left <= right:
            mid = (left + right) // 2

            # Convert virtual index back to actual array index
            actualMid = oldIdx(mid)

            if nums[actualMid] == target:
                return actualMid
            elif nums[actualMid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
            







        
        