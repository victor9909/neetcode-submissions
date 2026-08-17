class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if i not in count:
                        return False
                    count[i] -= 1
        
        return True