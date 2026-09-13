# Session 3, attemtp 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count2words = {}

        for word in strs:
            countOfLtrs = [0] * 26

            for ltr in word:
                idx = int(ord(ltr) - ord('a'))
                countOfLtrs[idx] += 1
            tupleCount = tuple(countOfLtrs)
            
            if tupleCount in count2words:
                count2words[tupleCount].append(word)
            else:
                count2words[tupleCount] = [word]

        return list(count2words.values())