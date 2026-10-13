class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        nums[0] + nums[1] == sum(nums)

        i'm trying to think if we can somehow figure out the relationships so that i'm only looking for subsets of this array (to stay pos or neg, still unsure)


        nums[0] == sum(nums) - nums[1]
        nums[0] - nums[1] == target

        sum(nums) - nums[1] - nums[1] == target


        -2nums[1] == target - sum(nums)

        -2(val subset we want to negate)  == target - sum(nums)

        (val subset we want to negate) == (target - sum) / -2

        (val subset we want to negate) == (sum - target) / 2

        x = (sum - target) / 2

        if (sum - target) is ever negative or odd --> return impossible (0)

        so really now the question is what is number of subsets that we can find that sum up to x.

        because its subset and not subsequnece -- i won't really think about sliding window or prefix here. rather i'm going to think of using dp. and we can use each number at most once so we have a bounded knapsack

        so i'll have a loop that goes through each number
            and then i'll have a second loop traversing the dp array: dp array where each index is a state val all going up to the last index of x. 
                and at each position i'll do 
                    dp[state_val] = dp[state_val - num] + 1 i think. lets try
        """
        diff = sum(nums) - target 
        if diff < 0 or diff % 2 != 0:
            return 0
        
        x = diff // 2

        #nums = [2,2,2], target = 2
        # x= 2


        dp = [0] * (x + 1)
        dp[0] = 1

        #   [0, 1, 2]
        #dp=[1, 0, 1]

        for n in nums:
            for state_val in range(x, n-1, -1):
                dp[state_val] += dp[state_val - n]

        return dp[-1]









