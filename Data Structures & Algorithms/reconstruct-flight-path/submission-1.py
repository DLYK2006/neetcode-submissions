from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = defaultdict(list)
        self.result=[]
        for a,b in tickets:
            self.graph[a].append(b)
        
        for airport in self.graph:
            self.graph[airport].sort()
        self.total = len(tickets)    
        self.result.append('JFK')
        self.dfs('JFK')
        return self.result

    def dfs(self,airport):
                # success: every ticket used → itinerary complete
        if len(self.result) == self.total + 1:
            return True

        # try each neighbor in lexical order
        for i in range(len(self.graph[airport])):
            next_airport = self.graph[airport][i]
            # CHOOSE: use this ticket
            self.graph[airport].pop(i)
            self.result.append(next_airport)
            # RECURSE
            if self.dfs(next_airport):
                return True
            # UNDO: this ticket led to a dead end, put it back
            self.graph[airport].insert(i, next_airport)
            self.result.pop()