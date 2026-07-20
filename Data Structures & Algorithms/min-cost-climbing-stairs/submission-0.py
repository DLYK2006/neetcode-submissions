class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost=cost
        self.cache=[0]*len(cost)
        return min(self.helper(0),self.helper(1))
       
    def helper(self,i):
        if i>=len(self.cost):
            return 0

        if self.cache[i]!=0:
            return self.cache[i]
            
        self.cache[i]=self.cost[i]+min(self.helper(i+1),self.helper(i+2))
        return self.cache[i]