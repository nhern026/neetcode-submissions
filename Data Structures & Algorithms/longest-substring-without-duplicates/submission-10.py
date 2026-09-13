# Session 1, Attempt 2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        seen = set()
        start = 0

        for end, char in enumerate(s):
            while char in seen:
                seen.remove(s[start])
                start += 1
            longestLength = max(longestLength, (end - start + 1)) 
            seen.add(char)
        return longestLength
