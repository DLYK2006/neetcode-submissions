class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache={}

        def helper(i,target):
            if target==amount:
                return 1
            elif target>amount:
                return 0

            if i>=len(coins):
                return 0

            if (i,target) in cache:
                return cache[(i,target)]
            
            result=0
            take=helper(i,target+coins[i])
            skip=helper(i+1,target)
            result=take+skip
            cache[(i,target)]=result
            return result
        
        return helper(0,0)
