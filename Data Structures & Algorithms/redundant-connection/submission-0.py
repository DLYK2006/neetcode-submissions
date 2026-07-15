class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[]
        for i in range(len(edges)):
            parent.append(i+1)

        def find(x):
            while parent[x-1]!=x:
                x=parent[x-1]
            return x
        
        def check(a,b):
            rootA,rootB=find(a),find(b)
            if rootA==rootB:
                return False
            parent[rootA-1]=rootB
            return True

        for i in range(len(edges)):
            a,b=edges[i]
            if check(a,b)==False:
                return edges[i]
            