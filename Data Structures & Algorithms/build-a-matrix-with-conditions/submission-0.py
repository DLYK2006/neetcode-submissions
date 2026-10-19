class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowgraph=defaultdict(list)
        colgraph=defaultdict(list)
        for a,b in rowConditions:
            rowgraph[a].append(b)
        for a,b in colConditions:
            colgraph[a].append(b)
        
        def getorder(graph):
            order=[]
            visited=set()
            visiting=set()

            def dfs(u):
                if u in visiting:
                    return False
                if u in visited:
                    return True
                visiting.add(u)

                for i in graph[u]:
                    if not dfs(i):
                        return False
                visiting.discard(u)
                visited.add(u)
                order.append(u)
                return True
            
            for i in range(1,k+1):
                if i not in visited:
                    if not dfs(i):
                        return []
            
            return order[::-1]
        
        roworder=getorder(rowgraph)
        colorder=getorder(colgraph)

        if not roworder or not colorder:
            return []
        
        row_map={val: idx for idx, val in enumerate(roworder)}
        col_map={val:idx for idx,val in enumerate(colorder)}

        print(row_map)
        print(col_map)

        matrix=[]                
        for i in range (k):
            matrix.append([])
            for m in range(k):
                matrix[i].append(0)
        
        for i in range(1,k+1):
            matrix[row_map[i]][col_map[i]]=i
        
        return (matrix)
