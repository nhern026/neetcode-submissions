class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for word in strs:
            length = len(word)
            encoded_str+= str(length)
            encoded_str+= "!"
            encoded_str+= word

        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]: #idx + 1, idx + lenght
        # if len(s) == 2:
        #     return [""]

        res = []
        idx = 0
        while idx < len(s): #runs this loop for each word in s
            word_length = ""
            word = ""
            while s[idx] != "!":
                word_length += s[idx]
                idx+=1

            word_length = int(word_length)
            for _ in range(word_length):
                idx+=1 
                word+= s[idx]
            
            res.append(word)
            idx += 1


        return res


