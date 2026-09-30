# Session 2, attept 1: 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
##
# coins = [1,5,10], amount = 12
# outputs = 3 <-- min amount of coings to reach tgt amount
#   
# only pos ints in the array, at least one coin value
# amount >= 0
# 

# try greedy (made sense in my head when i first saw it, but found counterexample)
# coins = [1, 3, 8, 9] amt = 11
# greedy returns = 3
# but in reality, it shoudl be: 2, so can't do greedy

# what if we broke it up into subproblems
# in my head if we choose one coin, now we have a certain amount to reach left, now i ask myself, how any coins do i need for that amount!
# like for example, working in the array, if i chose 9
# then i have 1 left to reach
# so then how many coins do i need to reach 1? --> 1
# so lets do DP approach where each subproblem is a given amount of $$ to reach, and we ask, how many coins do we need to reach that $$. 
# baseslines are 
    # if the amount left is in the memo
    #if the amount left is the amount left is in the list of coints (return 1)
    # if the amount left is zero, return 
    #or if the amount left is less than zero (not valid), return math.inf

# the reason DP is good here is because we'll see the same amount of $$ to make going down different recursive paths, for example. we may end up in a situation where we only need one coin once, let's say we chose 9+1 (so amt left is 1), and we figure out it needs 1 more coin in that situation, then when we are calculating 8+2, we also have the same amt left and so 1 more in that situation works as well.we don't watn to do the same work twice for the one coing so cacheing it in memory would be the fastest way to prevent duplicate work and fidn solutions.

# big o time is O(amount * len(coins))
# big o space is O(amount) <-- for the cache. recursion depth is (+ amount/min_coin_size)


        # coins = [1, 2], amount = 3

        memo = {}
        coin_set = set(coins)
        def coins_for_tgt(tgt):
            if tgt in coin_set:
                return 1
            if tgt == 0:
                return 0
            if tgt in memo:
                return memo[tgt]
            if tgt < 0:
                return math.inf

            min_coins_needed = math.inf
            for c in coins:
                # could add some slight optimization here to stop if c > tgt
                min_coins_needed = min(min_coins_needed, coins_for_tgt(tgt - c))
            
            memo[tgt] = min_coins_needed + 1 # plus wtvr coin we used to get there, 1: 2
            return memo[tgt]



        res = coins_for_tgt(amount)
        return res if res < math.inf else -1

    # if amount = 10,000 then this. might break if one of the coins was 1, we would have a recurusio dpeth of 10,000 and so that would exceed the recursion limit and this would crash. To solve this we can do the bottom up approach and use an array instead. 

