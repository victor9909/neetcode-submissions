class Solution:

    def encode(self, strs: List[str]) -> str:
        to_send = ''
        for s in strs:
            to_send += str(len(s)) + '#' + s + "#"
        return to_send

    def decode(self, s: str) -> List[str]:

        res = []
        idx = 0
        while idx < len(s):
            word_len = ''
            while s[idx] != "#":
                word_len += s[idx]
                idx += 1
            idx += 1
            count = 0
            word = ""
            print(word_len)
            while count < int(word_len):
                word += s[idx]
                count += 1
                idx += 1
            res.append(word)
            idx +=  1


        return res


