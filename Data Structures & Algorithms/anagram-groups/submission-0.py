class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        DNAcollection = {}
        res = []

        for word in strs:
            wordDNA = {}
            for ltr in word:
                wordDNA[ltr] = 1 + wordDNA.get(ltr, 0)

            if tuple(sorted(wordDNA.items())) not in DNAcollection:
                res.append([word])
                DNAcollection[tuple(sorted(wordDNA.items()))] = len(res)-1 #save the idx where we put it
            else:
                res[DNAcollection[tuple(sorted(wordDNA.items()))]].append(word)
        
        return res

