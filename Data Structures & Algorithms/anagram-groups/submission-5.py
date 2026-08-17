class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_groups = defaultdict(list)
        for s in strs:
            bit_arr = [0] * 26
            for c in s:
                bit_arr[ord('z') - ord(c)] += 1
            dict_groups[tuple(bit_arr)].append(s)
        return list(dict_groups.values())