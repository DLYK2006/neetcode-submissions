class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache={}
        A=[1]+nums+[1]
        
        def helper(l,r):
            
            if l+1==r:
                return 0
            
            if(l,r) in cache:
                return cache[(l,r)]

            maximum=0
            for k in range(l+1,r):
                coins=helper(k,r)+helper(l,k)+(A[k]*A[l]*A[r])
                maximum=max(coins,maximum)
            
            cache[(l,r)]=maximum
            return cache[(l,r)]
        
        return helper(0,len(A)-1)