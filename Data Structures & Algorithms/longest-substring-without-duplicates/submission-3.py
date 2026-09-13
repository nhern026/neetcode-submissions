# Session 1, Attemp 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        currentLength = 0
        char2ID = {}

        for idx, char in enumerate(s):
            if char in char2ID: 
                startOfSubstringIDX = idx - currentLength
                if char2ID[char] >= startOfSubstringIDX: #in current substring
                    currentLength = idx - char2ID[char]
                else:
                    currentLength += 1
            else:
                currentLength += 1
            char2ID[char] = idx
            longestLength = max(currentLength, longestLength)
        return longestLength

