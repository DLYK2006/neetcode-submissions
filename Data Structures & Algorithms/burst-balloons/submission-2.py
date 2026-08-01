class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache={}
        grah=[1]+nums+[1]

        def helper(l,r):

            if l+1==r:
                return 0
            
            if (l,r)in cache:
                return cache[(l,r)]

            maximum=0
            for k in range(l+1,r):
                coins=helper(l,k)+helper(k,r)+(grah[l]*grah[k]*grah[r])
                maximum=max(maximum,coins)
            
            cache[(l,r)]=maximum
            return cache[(l,r)]
        
        return helper(0,len(grah)-1)
