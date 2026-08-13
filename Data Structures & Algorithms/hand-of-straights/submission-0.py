from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        frequencies=defaultdict(int)
        hand=sorted(hand)

        for i in hand:
            frequencies[i]+=1

        for card in hand:
            count=frequencies[card]

            if count==0:
                continue
            for i in range(groupSize):
                target=card+i
                if frequencies[target]<count:
                    return False
                frequencies[target]-=1
        
        return True
