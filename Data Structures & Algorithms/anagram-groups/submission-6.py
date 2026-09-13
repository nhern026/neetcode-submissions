class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dna2Wrds = defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for char in word: 
                arr[ord(char) - ord("a")] += 1
            dna2Wrds[tuple(arr)].append(word)
        
        res = []
        for key, vals in dna2Wrds.items():
            res.append(vals)

        return res
