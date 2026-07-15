class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]      # each node is its own root
        round=0

        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        
        def union(a,b):
            rootA,rootB=find(a),find(b)
            if rootA==rootB:
                return False
            parent[rootA]=rootB
            return True
        
        components=n
        for a,b in edges:
            if union(a,b):
                components-=1
        return components