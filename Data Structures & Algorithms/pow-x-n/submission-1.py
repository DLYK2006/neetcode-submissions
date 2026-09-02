class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def rec(x,n):
            if x==0:
                return 0.0
            if n==0:
                return 1.0
            
            half=rec(x,n//2)
            if n%2==0:
                return half*half
            else:
                return half*half*x
        
        answer=rec(x,abs(n))
        if n<0:
            return (1/answer)
        else:
            return answer