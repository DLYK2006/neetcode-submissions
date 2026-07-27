class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}

        def helper(a,target):
            if a>=len(coins):
                return 0
            
            if target==amount:
                return 1
            elif target>amount:
                return 0
            
            if (a,target) in cache:
                return cache[(a,target)]

            result=0
            for i in range(a,len(coins)):
                result+=helper(i,target+coins[i])
            cache[(a,target)]=result          
            return cache[(a,target)]
        
        return helper(0,0)
        
            
