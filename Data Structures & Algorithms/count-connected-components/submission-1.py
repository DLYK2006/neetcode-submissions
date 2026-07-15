class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.graph={}
        rounds=0
        for a in range(n):
            self.graph[a]=[]
        for a,b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)

        visit=set()
        for i in range(len(self.graph)):
            if self.graph[i]!=-1:
                self.dfs(i,visit)
                rounds+=1
        
        return rounds

    def dfs(self,node,visit):
        if node in visit:
            return 
        visit.add(node)
        for i in self.graph[node]:
            self.dfs(i,visit)
        self.graph[node]=-1
        
