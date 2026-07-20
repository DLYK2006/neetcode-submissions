class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices=[float("inf")]*n
        prices[src]=0
        

        for i in range(k+1):
            temp=prices.copy()
            for flight in flights:
                u,v,cost=flight
                if prices[u]!=float("inf"):
                    temp[v]=min(temp[v],prices[u]+cost)
            prices=temp
        
        if prices[dst]!=float("inf"):
            return prices[dst]
        else:
            return -1

