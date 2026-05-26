import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=1
        middle=(left+right)//2

        while left<right:
            time=0
            print(left)

            for i in range(len(piles)):
                time+=math.ceil(piles[i]/middle)
            if(time>h):
                left=middle+1
                middle=(left+right)//2
            elif(time<=h):
                right=middle
                middle=(left+right)//2
        return left