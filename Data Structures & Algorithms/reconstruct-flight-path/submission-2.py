from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = defaultdict(list)
        self.result=[]
        for a,b in tickets:
            self.graph[a].append(b)
        
        for airport in self.graph:
            self.graph[airport].sort()

        self.dfs('JFK')
        new=self.result[::-1]
        return new

    def dfs(self,airport):
        while self.graph[airport]:
            next_airport = self.graph[airport].pop(0)   
            self.dfs(next_airport)
        self.result.append(airport)