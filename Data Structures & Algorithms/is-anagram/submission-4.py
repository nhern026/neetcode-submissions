from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDNA = Counter(s)
        tDNA = Counter(t)
        return sDNA == tDNA