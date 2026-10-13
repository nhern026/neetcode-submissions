class Solution:
    def numSquares(self, n: int) -> int:
        # when do we stop updating n??

        # when the perfect square we are using is larger than n
        # so then we need to generate all the perfect squares up until == n

        # right so lets do that 

        perf_squares = []
        sq = 1
        while sq**2 <= n:
            perf_squares.append(sq**2)
            sq += 1

        # we can use as many as we like so we are unbounded, forward pass --> 
        dp = [math.inf] * (n+1)
        dp[0] = 0

        # n = 6
        #sq's = [1, 4]
        #dp = [0, inf, inf, inf, inf, inf, inf]
        #      0,  1,   2,   3,   4,   5,   6

        # after first pass
        #dp = [0, 1, 2, 3, 4, 5, 6] <-- if we could only use 1

        #after second pass
        #dp = [0, 1, 2, 3, 4, 5, 6]

        for sq in perf_squares:
            for n in range(sq, n+1):
                dp[n] = min(dp[n], dp[n-sq] + 1)

        
        return dp[-1]










