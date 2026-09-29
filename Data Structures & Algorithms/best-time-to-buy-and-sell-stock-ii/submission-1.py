class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache={}

        def helper(i,hold):
            if (i,hold) in cache:
                return cache[(i,hold)]
            
            if i==len(prices):
                return 0
            
            profit=helper(i+1,hold)
            if hold is False:
                profit=max(profit,-prices[i]+helper(i+1,True))    
            else:
                profit=max(profit,prices[i]+helper(i+1,False))
            
            cache[(i,hold)]=profit
            return profit
        
        return helper(0,False)
            
            

            
            

            

            
