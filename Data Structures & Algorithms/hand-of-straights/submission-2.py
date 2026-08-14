from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        frequencies=defaultdict(int)
        hand=sorted(hand)
        for i in hand:
            frequencies[i]+=1
        
        for pick in hand:
            if frequencies[pick]==0:
                continue

            for i in range(pick,pick+groupSize):
                if frequencies[i]==0:
                    return False
                frequencies[i]-=1
        
        return True
