class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        symbol = "#"
        for s in strs:
            offset = len(s)
            res += str(offset) + symbol + s

        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            str_len = int(s[i:j])
            start = j + 1
            next_start = start + str_len
            res.append(s[start:next_start])

            i = next_start
        
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))