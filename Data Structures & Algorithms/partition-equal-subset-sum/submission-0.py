class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #all nums are positive
        """
        lets think backtracking first
        we use a number or not use a number
            either way we move our index up

        but you'll notice that we can end up in the siutaiton where our sum is 3 twice
            and we ask when our index is pointing at the last element. we are doing repeated wokr

            # 1 + 2 == 3. state(3, idx=3)
            # 3 == 3. state(3, idx=3)
            # so we are doing repeated work and should do DP approach

        # lets think bottom up approach

        okay so lets look at the list:
        [1,2,3,4] = sums to 10

        bascially going up to each moment here we can either use or not use a number
        so then lets represent our states with 0...target
            reminder that our target == sum/2
        
        dp=[0, 1, 2, 3, 4, 5] (i put idx as vals but we'll start each as False)
        each state is a number with our target number last
        at each state we are going to decide if its true or not that we can make a subset that equals that number

        okay great, so lets do the base case, can we do 0?? yes alwyas because we can take the empty subset, so that's our base case, great lets set dp[0] = True

        now we have
            0, 1, 2, 3, 4, 5
        dp=[T, F, F, F, F, F

        now how do we know if we can make one with 1???, well that's where our loop can come in and we can use each of the numbers in our original array and see if we can add to them. so great

        starting with the first element: 1 (basically asking if i only had 1 can i reach any of these states)

            0, 1, 2, 3, 4, 5
        dp=[T, F, F, F, F, F

        the relationship should be for a given state, is the state at dp[state_val - num] == True? if so we can get to that state by adding just our number. 

        now if we did a forward loop we know that it would all return true, so we need to do a backwards loop as to not count our 1 mulitple times. 

        after doing so we get this: 
            0, 1, 2, 3, 4, 5
        dp=[T, T, F, F, F, F]

        # now lets try 2!
            0, 1, 2, 3, 4, 5
        dp=[T, T, T, T, F, F] notice here how 3 is true even though we haven't even used 3 yet

        # now lets try 3
            0, 1, 2, 3, 4, 5
        dp=[T, T, T, T, T, T] <-- all true!! 

        # now lets try 4
            0, 1, 2, 3, 4, 5
        dp=[T, T, T, T, T, T] nothing changes ofc

        this solution is O(|nums| * sum(nums)/2)
        space time is O(sum(nums)/2)
        """

        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)//2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for state_val in range(target, n-1, -1):
                dp[state_val] = dp[state_val] or dp[state_val-n]

        return dp[-1]








