# Session 3, attemtp 1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count2words = defaultdict(list)

        for word in strs:
            countOfLtrs = [0] * 26

            for ltr in word:
                idx = int(ord(ltr) - ord('a'))
                countOfLtrs[idx] += 1

            count2words[tuple(countOfLtrs)].append(word)

        return list(count2words.values())