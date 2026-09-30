class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    
    

    # can't sort because we need it to be in order of original idxs

    # alwayas integer elements
    # numbers can be both negative and positive and 0
    # nums always has at least one element
    # can i modify nums if i need to? yes
    
    # so i need to find the length of the longest subsequence of numbers in this array

    # some examples: 
    # [9], 1
    # [0], 1
    # if there's only one number, always 1
    # [0, 1], 2
    # [-10, 0], 2
    # [1, 0], 1
    # [0, -10], 1

    # i'm thinking we can do a backtracking approach that calculates all of the subseqeunecs possible and only compares a max length list for those that are in increasing order. if we add a number that is bigger than the prev number in the current subsqeuence, we don't go down that path or compare max
    # this would calculate all subsequneces in the worst case so that's O(2^N) where N is len(nums). that is pretty terrible for large N's.
        # the issue with this is that lets say we have the list 1, 2, 3. when we go down 1 all the way we get the subeqeuence 1, 2, 3. when we go with 2 as the start we sovle for 2, 3. That's doing repeated work we. So intead there must be some dp approach, let's think of a bototm up solution: 
    # so initiailly i'm thinking if we start at the last number and intilize that with dp[-1] = 1. then work our way backwards, at each node we look ahead to find a val that is higher, and keep the max lenght is has already in there. you do this for all numbers and return the dp[i] where i has dp[i] the highest. 
    #that is a time O(n^2) approach and a big O(n) for space because we only use one array.

        N = len(nums)
        dp = [1] * N
        # nums = [1, 2, 2, 3], N= 4
        # dp =   [1, 2, 2, 1], i= 0 j=3, max_length = 2 (i went through whole dry run)

        for i in range(N-2, -1, -1):
            max_length_ahead = 0
            for j in range(i+1, N): #0-3  N=4
                if nums[i] < nums[j]: # checking nums
                    max_length_ahead = max(max_length_ahead, dp[j])

            dp[i] += max_length_ahead
            
        return max(dp)
