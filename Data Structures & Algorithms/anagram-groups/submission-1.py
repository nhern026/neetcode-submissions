class Solution:
    #this function loops through the entire collection of words. It creates a dictionary (DNA) for each word, and then uses the tupled version of that as a key in another dictionary that tracks that corresponding dna's list in the res list. like apple's dna will point to the idx where apple is stored in the results. Very ineffecient though. time: 

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        DNAcollection = {}
        res = []

        for word in strs:
            wordDNA = {}
            for ltr in word:
                wordDNA[ltr] = 1 + wordDNA.get(ltr, 0)

            tupledDNA = tuple(sorted(wordDNA.items()))
            if tupledDNA not in DNAcollection:
                res.append([word])
                DNAcollection[tupledDNA] = len(res)-1 #save the idx where we put it
            else:
                res[DNAcollection[tupledDNA]].append(word)
        
        return res
