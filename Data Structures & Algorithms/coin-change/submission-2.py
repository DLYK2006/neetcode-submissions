class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={}

        def helper(amount):
            if amount==0:
                return 0
            if amount in cache:
                return cache[amount]
            
            result=float('inf')

            for coin in coins:
                if amount-coin>=0:
                    result=min(1+helper(amount-coin),result)
            
            cache[amount]=result
            return result
        
        if helper(amount)==float('inf'):
            return -1
        else:
            return helper(amount)
            



            


            
