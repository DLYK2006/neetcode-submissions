class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={}

        def helper(i):
            if i in cache:
                return cache[i]
            if i>=len(cost):
                return 0
            
            result=cost[i]+min(helper(i+1),helper(i+2))

            cache[i]=result
            return result
        
        return min(helper(0),helper(1))