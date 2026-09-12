class Solution:

    # Hello, World
    # 5#Hello5#World

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
        
    # 5#Hello5#World
    # Hello, World
    def decode(self, s: str) -> List[str]:

        i = 0
        res= []
        while i < len(s):

            n = ""
            while s[i] != "#":
                n += s[i]
                i += 1
            
            len_w = int(n)
            i += 1
            res.append(s[i: i + len_w])
            i += len_w
        return res







