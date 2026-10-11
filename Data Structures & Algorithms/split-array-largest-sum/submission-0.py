# Session 1, attempt 1: needed hint from calude after i realized we needed to do binary search. claude said we are searching over the possible answers. upon hearing that i was able to design the rest. fahhh
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        nums = [2, 4, 10, 1, 5]

        how would i treat this for k = 2
        i would find the sum, and then make a split starting at the first index
            index 0 = nums[0] = 2
        and find the sum for each side of that index (the first subarray includes that index)
            by using the sum we found before and subtracting by the sum of the current subarray (easily found)
            compare the max of both sides (left_sum, right_sum) to the current running min we have
                and set min=(best_min, max(left_sum, right_sum))

                although here i see that i'm trying minimize a max, so maybe binary search can come into play


        nums = [2, 4, 2, 1, 5] k = 3

        biggest possible value = 2 + 4 + 2 + 1 + 5 = 14
        largest value possible in a single subarray of size 1 = 5

        so then i gotta search between 5 --> 14
        so i try out lets say 7 (bc why not for now). can i spllit these subarray into k parts wihout having any go over 7??
            lets think abt it, hmmm
            i could do a greedy approach where i make the first subarary by adding each number i see until the number i want to add makes it go over 7. 
            lets try

            first subarray = [2, 4]
            second subarray = [2, 1]
            third subarray = [5]

            that is 3 subarrays. if k >= 3 then we're good. if k < 3 then we're not good. 

            okay so 7 is a possible answer, now the possible answers are between 5 and 7

            lets try 6

            first subarray = [2, 4]
            second subarray = [2, 1]
            third subarray = [5]

            that is 3 subarrays, if k >= 3 then we're good. if k < 3 then we're not good. 

            now the possible answers are between 5 and 6

            lets try 5
            first subarray = [2]
            second subarray = [4]
            third subarray = [2, 1]
            fourth subarray = [5]

            that is 4 subarrays. if k >= 4 then we can say we're good. if k < 4 then wer'e not good
            k is 3 whcih is < 4. so not good. l = mdi + 1 l = 5 + 1 l = 6

            l,r = 6 so we return 6


            our right pointer is the valid truth,  it will alwyas be true so we set r = mid each time
            l is our hopeful pointer, it doesn't have to be true, so we set l = mid + 1 whenever we fail

            time: O(log(sum(nums) - max_val) * n)
            space: O(1) potentially with usign running sum in subarray calcs
        """

        l = max(nums) # l doesn't have to be valid
        r = sum(nums) # r must always be a valid answer

        while l < r:
            mid = (l+r)//2

            # can mid work?
            subarray_count = 0
            running_sum = 0
            for n in nums:
                if running_sum + n > mid:
                    subarray_count += 1
                    running_sum = n
                else:
                    running_sum += n

            subarray_count += 1 # DON"T FORGET THIS OFF BY 1 ERROR

            if subarray_count <= k:
                print(mid)
                print(subarray_count)
                print()
                r = mid
            else:
                l = mid + 1

        return r


