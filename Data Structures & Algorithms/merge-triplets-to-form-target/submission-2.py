class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found0=False
        found1=False
        found2=False

        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            if a==target[0]:
                found0=True
            if b==target[1]:
                found1=True
            if c==target[2]:
                found2=True
        
        if found0 and found1 and found2:
            return True
        else:
            return False