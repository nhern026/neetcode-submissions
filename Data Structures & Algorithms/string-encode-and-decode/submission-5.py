# Session 2, attempt 1
class Solution:

    def encode(self, strs: List[str]) -> str:
        listOfWordsWithLength = []
        
        for word in strs:
            length = len(word)
            listOfWordsWithLength.append(str(length) + "!" + word)
        
        return "".join(listOfWordsWithLength)

    def decode(self, s: str) -> List[str]:
        idx = 0
        res = []

        while idx < len(s):
            numba = ""
            while s[idx].isdigit():
                numba += s[idx]
                idx += 1
            
            idx += 1 #because now idx is on !

            word_holder = []
            for _ in range(int(numba)):
                word_holder.append(s[idx])
                idx += 1
            
            res.append("".join(word_holder))

        return res


