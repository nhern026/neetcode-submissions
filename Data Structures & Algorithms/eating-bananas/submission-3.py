# Session 1, attempt 1: did a while loop to caluclate hours_spent but that should have been 
    # math.ceil(pile / mid_rate)
# 12:55 --> 1:10 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [1, 4, 3, 2] h = 9

        # if h = len(piles) then answer is max of that piles
        # if h is really large, we could potentially just do 1
        # so we have a range of 1 --> max(val)
        # we can try each value and see what works
        # or we can do a binary search to find the value and make it nlogm
            # n because we'd have to try out the piles each time

        # for k = 2

        # k = 2 
        # hours_spent = 0
        # [1, 4, 3, 2]
        # [-1, 4, 3, 2] hours_spent = 1
        # [-1, 0, 3, 2] hours_spent = 3
        # [-1, 0, -1, 2] hours_spent = 5
        # [-1, 0, -1, 0] hours_spent = 6 (yes we can)
        # for pile in piles:
        #     while pile > 0:
        #         pile -= k
        #         hours_spent += 1
        
        # 1, 2, 3, 4
        slower, faster = 1, max(piles)

        while slower < faster:
            mid_rate = (faster + slower) // 2

            hours_spent = 0

            for pile in piles:
                hours_spent += math.ceil(pile/mid_rate)
            
            if hours_spent <= h:
                # it works so
                faster = mid_rate 
                # we want slow --> fast to have the range of possible answers
                # and since we want the slowest possibel answer, we update fastest
                # to the slowest time we have found so far
            else:
                slower = mid_rate + 1 
                # + 1 here becuase mid_rate is not a possible solution
        
        return faster