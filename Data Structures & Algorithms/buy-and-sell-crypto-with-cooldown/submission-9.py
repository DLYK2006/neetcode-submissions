class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache={}

        def helper(i,bought):
            if i>=len(prices):
                return 0
            
            if (i,bought) in cache:
                return cache[(i,bought)]
            
            if bought==False:
                buy=helper(i+1,True)-prices[i]
                save=helper(i+1,False)
                cache[(i,bought)]=max(buy,save)
            else:
                sell=helper(i+2,False)+prices[i]
                hold=helper(i+1,True)
                cache[(i,bought)]=max(sell,hold)
            
            return cache[(i,bought)]
        
        return helper(0,False)
            