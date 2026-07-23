class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache=[]
        for i in range(amount+1):
            cache.append(None)
        
        def dfs(amount):

            if amount<0:
                return float('inf')
            if amount==0:
                return 0
            
            if cache[amount] is not None:
                return cache[amount]

            res = float('inf')
            for i in range(len(coins)):
                res = min(res, 1 + dfs(amount - coins[i]))
            
            cache[amount] = res
            return cache[amount]

        result=dfs(amount)
        return result if result!=float('inf') else -1