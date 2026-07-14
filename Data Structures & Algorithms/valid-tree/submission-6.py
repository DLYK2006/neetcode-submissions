class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.graph={}
        for a in range(n):
            self.graph[a]=[]
        for a,b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)  #gotta add this cuz you have to take into account the bidirection

        visit=set()
        if self.dfs(0,visit,-1)==False:
            return False
        else:
            return len(visit)==n

    def dfs(self,node,visit,past):
        if node in visit:
            return False
        visit.add(node)
        for i in (self.graph[node]):
            if i==past:
                continue
            if self.dfs(i,visit,node) is False:
                return False
        return True
    
    

