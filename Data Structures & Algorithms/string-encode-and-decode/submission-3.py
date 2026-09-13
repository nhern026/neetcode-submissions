# Session 1, attempt 2. Cleaning it up and makign it more effecient. 

# take a look at the differences of how i collected strings.
    # instead of adding into a string by doing += i'm actually making a list. 
    # here's why: 
        # when you do += with a string, it copies and makes a new string
        # so over time that becomes really ineffecient. 
            # INSTEAD it's better to make a list and append to it.
            # that way you only use those characters twice, 
            # once when you add it to the list, and the other when you join. 
            # rather than, lets say the first char is "s", if you have 5 words
            # that char "s" is copied and adressed to a new spot 5 times!

# also made the word collection in decode by slicing and not by looping. 
# its just mainly cleaner, bc it still takes O(m) where m is word length
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str_list = []
        
        for word in strs:
            encoded_str_list.append(str(len(word)) + "!" + word)

        return "".join(encoded_str_list)

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0

        while idx < len(s):
            word_length_List = []

            while s[idx] != "!": 
                word_length_List.append(s[idx])
                idx+=1

            word_length = int("".join(word_length_List))
            word_start = idx + 1
            word_end = idx + 1 + word_length

            res.append(s[word_start : word_end])
            
            idx = word_end

        return res

        


