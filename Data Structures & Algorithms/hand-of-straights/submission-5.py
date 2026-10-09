class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool: 
        if len(hand)%groupSize!=0:
            return False
        
        hand=sorted(hand)

        frequency=defaultdict(int)
        for i in hand:
            frequency[i]+=1
        
        for i in hand:
            if frequency[i]==0:
                continue

            for m in range(i,i+groupSize):
                if frequency[m]==0:
                    return False
                else:
                    frequency[m]-=1
            
        return True

        
