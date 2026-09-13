# Session 1, Attemp 1: Brute Force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap.remove(key) don't think i have to i just have to smart check

        longestLength = 0
        currentLength = 0

        char2ID = {}
        workingString = ""

        couonter = 1
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

