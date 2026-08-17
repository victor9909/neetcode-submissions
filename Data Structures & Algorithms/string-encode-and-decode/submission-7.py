class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            start_idx = idx
            
            while s[idx] != "#":
                idx += 1
            len_s = int(s[start_idx: idx])
            res.append(s[idx + 1: idx + 1 + len_s])
            idx = idx + 1 + len_s
        return res
            
            