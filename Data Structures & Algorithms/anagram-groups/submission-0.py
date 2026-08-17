class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    
    # strs = ["act","pots","tops","cat","stop","hat"]
    # act -> 001001000..
    # pots -> 001001001..
    # hat -> 101001001...
    # {001001000: [act, cat], 001001001: [pots, tops, stop], 101001001: [hat]}
    # [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        dict_res = defaultdict(list)
        for s in strs:
            bit_arr = [0] * 26
            for c in s:
                bit_arr[ord('z') - ord(c)] += 1
            dict_res[tuple(bit_arr)].append(s)
        
        return list(dict_res.values())