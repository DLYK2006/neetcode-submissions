class Solution:
    def arrangeCoins(self, n: int) -> int:
        number=1
        while n>0 and n>=number:
            n=n-number
            if n<0:
                break
            number+=1
        
        return number-1