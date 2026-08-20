class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        dict_order = {}
        for i, o in enumerate(order):
            dict_order[o] = i
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if dict_order[w1[j]] > dict_order[w2[j]]:
                        return False
                    break
        
        return True
            