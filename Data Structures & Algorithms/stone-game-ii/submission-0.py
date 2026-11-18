class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        suffixsum=[0]*(len(piles)+1)

        for i in range(len(piles)-1,-1,-1):
            suffixsum[i]=piles[i]+suffixsum[i+1]
        
        cache={}

        def helper(i,M):
            if (i,M) in cache:
                return cache[(i,M)]    
            if i>=len(piles):
                return 0
            if i+2*M>=len(piles):
                return suffixsum[i]
            
            result=0
            for X in range(1,2*M+1):
                bob=helper(i+X,max(M,X))
                alice=suffixsum[i]-bob
                result=max(alice,result)
            
            cache[(i,M)]=result
            return result
        
        return helper(0,1)

