class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper=max(piles)
        lower=1
        middle=(upper+lower)//2

        while upper>lower:
            hour=0
            for i in piles:
                hour+=math.ceil(i/middle)
            if hour>h:
                lower=middle+1
            elif hour<=h:
                upper=middle
            middle=(upper+lower)//2
        
        return (lower)
