# Session 2, attempt 1
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        WORDSET = set()
        max_word_len = 0
        for word in wordDict:
            WORDSET.add(word)
            max_word_len = max(max_word_len, len(word))

        # #0. 1. 2. 3. 4. 5. 6. 7
        # "n, e, e, t, c, o, d, e"
        #  F. F. F. T. F. F. F. T

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i-1, -1, -1):
                if s[j:i] in WORDSET and dp[j]:
                    dp[i] = True
                    break

        return dp[-1]

        

