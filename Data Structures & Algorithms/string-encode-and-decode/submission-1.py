# Session 1, attempt 2
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str_list = []
        
        for word in strs:
            encoded_str_list.append(str(len(word)) + "!" + word)

        return "".join(encoded_str_list)

    def decode(self, s: str) -> List[str]: #idx + 1, idx + lenght
        res = []
        idx = 0

        while idx < len(s): #runs this loop for each word in s
            word_length_List = []
            word = ""
            while s[idx] != "!": #this loop collects the length of upcoming word
                word_length_List.append(s[idx])
                idx+=1

            word_length = int("".join(word_length_List))
            word_start = idx + 1
            word_end = idx + 1 + word_length

            res.append(s[word_start : word_end])
            
            idx = word_end


        return res

        


