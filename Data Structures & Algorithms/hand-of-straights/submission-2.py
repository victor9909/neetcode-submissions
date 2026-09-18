class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False
        
        
        cnt = Counter(hand)

        for n in sorted(hand):

            if cnt[n] > 0:
                
                freq = cnt[n]
                for i in range(n, n + groupSize):
                    if freq > cnt[i]:
                        return False
                    cnt[i] -= freq

        return True

