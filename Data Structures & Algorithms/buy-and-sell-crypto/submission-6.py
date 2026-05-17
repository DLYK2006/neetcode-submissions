class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0 
        profit=0
        right=1

        while right<len(prices):
            if(prices[right]-prices[left]>0):
                profit=max(profit,prices[right]-prices[left])
            else:
                left=right
            right+=1
        
        return profit