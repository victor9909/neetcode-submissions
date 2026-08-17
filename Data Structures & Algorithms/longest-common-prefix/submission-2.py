class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # strs = ["bat","bag","bank","band"]
        # b -> continue
        # ba -> continue
        # bat -> stop

        prefix = ""
        tmp = ""
        i = 0
        while True:
            if i > len(strs[0]) - 1:
                return prefix
            tmp += strs[0][i]
            for st in strs:
                if not st.startswith(tmp):
                    return prefix
            prefix = tmp
            i += 1

