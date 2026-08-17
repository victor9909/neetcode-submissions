class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_subs = defaultdict(list)
        for s in strs:
            bit_s = [0] * 26
            for c in s:
                bit_s[ord('z') - ord(c)] += 1
            dict_subs[tuple(bit_s)].append(s)
        return list(dict_subs.values())