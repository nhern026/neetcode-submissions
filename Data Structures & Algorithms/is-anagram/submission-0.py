class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntS = {}
        for ltr in s:
            if ltr not in cntS:
                cntS[ltr] = 0
            else:
                cntS[ltr] += 1

        cntT = {}
        for ltr in t:
            if ltr not in cntT:
                cntT[ltr] = 0
            else:
                cntT[ltr] += 1
        return cntT == cntS

        