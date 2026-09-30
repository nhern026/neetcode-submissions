class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #the text below is pretty rubsih. if i was doing is text 1 a subsequnece of text2, you can easily use a two pointer solution. the big O times below are  off i think. Next time just say i thought maybe backtracking coudl work but that woudlnt' be feasible as the texts can be as big as 1000 so even normal backtracking would never work 2^1000

        # well if i was trying to see if text1 was a subsequence in text2 i'd prob do some backtracking approach and cut it off when a built word is len(text1), and i'd return true if it is equal to it and recurse that up. this would be time O(2^n). BUT if we'd do that for each subsequence in text, then that'd be (2^m * 2^n). BUT what if we found all the subsequences of one of the texts save it in a set, and then as we build the the subsequences of the other text and as we go check if its in the set. That would be O(2^m + 2^n). The space complexity also jumps up to O(2^n). this approach is not feasible because the longest each text could be is 1000 which 2^1000 would be well abvoe the recursive limit of python (1000)

    # okay back to real world and not wtvr garbage i spewed above. 
    # if i had one text and asked are you a subsequnece of the text to our right: 
    # we can do start one pointer on text1 (L) and one pointer on text2 (R). keep advancing R until text2[R] = text1[L]. then advance L+=1 and keep moving R from there. keep doing that until L passes the end of the word, return True if so. 

    # so can we turn that into a subsequence vs subsequence version? 

    # yes we can! and i looked at the minimum edit distance neetcode video first and was able to use that solution to do this one. 

        len_1, len_2 = len(text1), len(text2)
        
        # intialize DP
        dp = []
        for i in range(len_1 + 1):
            row = []
            for j in range(len_2 + 1):
                row.append(math.inf)
            dp.append(row)

        for x in range(len_1 + 1):
            dp[x][-1] = 0
        for y in range(len_2 + 1):
            dp[-1][y] = 0

        for i in range(len_1-1, -1, -1):
            for j in range(len_2-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]