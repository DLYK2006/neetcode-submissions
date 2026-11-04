class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        cache={}

        def helper(i,m):
            if (i,m) in cache:
                return cache[(i,m)]
            
            if (m<=0):
                return 0
            elif(i==len(time)):
                return float('inf')

            result=0
            
            take=cost[i]+helper(i+1,m-1-time[i])
            skip=0+helper(i+1,m)

            result=min(take,skip)
            cache[(i,m)]=result
            return result

        return helper(0,len(time))


        pass
