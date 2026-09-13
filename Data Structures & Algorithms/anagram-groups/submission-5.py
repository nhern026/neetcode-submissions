#So here i learned a few things. but basically what is more effecient than my solution 1 is that i save time not having to sort since count is already ordered. this is smart because we KNOW there are 26 lowercase letters so we can just hold a count and each idx correlates to a letter. 
    #learned a cool way to match letters to idx with ord()
    #learned about defaultdict(...) 
    #learned that you can't use a list or hashmap as a key in a dict, so instead you can convert it to a tuple. but of course, if you tuple a hashmap you have to worry about ordering. tuples are order sensitive during comparisons.  

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        res = defaultdict(list) #mapping charCount to list of anagrams. defaultdict(list) just makes the default value a [] if the key doesn't exist when called
        for word in strs:
            count = [0] * 26 # a .. z

            for char in word:
                count[ord(char) - ord("a")] += 1 #because lowercase letters come after another
            
            res[tuple(count)].append(word)
        
        return list(res.values())



