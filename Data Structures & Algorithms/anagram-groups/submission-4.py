class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def build_bit_arr(s):
            bit = [0] * 26
            for c in s:
                bit[ord('z') - ord(c)] += 1
            return bit
        
        dict_anagrams = defaultdict(list)
        for s in strs:
            bit_s = build_bit_arr(s)
            dict_anagrams[tuple(bit_s)].append(s)
        
        return list(dict_anagrams.values())
