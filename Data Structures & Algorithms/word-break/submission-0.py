class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        WORD_DICT = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        # string[inclusive:exclusive], string[i:i] == ""
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                window = s[j:i] # should give everythign from index j through i
                if window in WORD_DICT and dp[j]:
                    dp[i] = True
                    break
    
        return dp[-1]

        # we know that s is at least one letter, there is at least one word in the worddict and all the words in the worddict are nonempty

        # we treat the subproblem asking at everything index: if this were the last index, would it be true? we figure that out by saying, if we can find a word thats in the dict with this letter as the last string, is the rest of the string before that word valid? 

        # big O time complexity is O(n^3) because we go through each letter and build backwards O(n^2) BUT it also takes O(n) time to build a string O(n^2 * n). # if we optimize to onyl go back max word length in word dict then O(n * l^2) because we go over all the ltters and only travle back L amount and build L sized arrays. 


        # big O space complexity is O(n)

        # we could optimize by stopping building windows bigger than the max len of a word in the worddict, this makes it 

                #   c a t s
                #   0 1 2 3
                # T F F F F
                # 0 1 2 3 4
                # 
                # i = 1, j = 0
                # 


