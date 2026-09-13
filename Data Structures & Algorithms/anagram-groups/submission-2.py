class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        res = defaultdict(list) #mapping charCount to list of anagrams
        for word in strs:
            count = [0] * 26 # a .. z

            for char in word:
                count[ord(char) - ord("a")] += 1 #because lowercase letters come after another
            
            res[tuple(count)].append(word)
        
        return list(res.values())



