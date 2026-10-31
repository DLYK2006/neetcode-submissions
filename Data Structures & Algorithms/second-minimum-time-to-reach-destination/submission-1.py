class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        short=[float('inf')]*(n+1)
        long=[float('inf')]*(n+1)

        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue=deque([(1,0)])

        while queue:
            node,curr_time=queue.popleft()
            if (curr_time//change)%2!=0:
                    curr_time=change*((curr_time//change)+1)

            for neighbours in graph[node]:
                arrive=curr_time+time
                if arrive<short[neighbours]:
                    long[neighbours]=short[neighbours]
                    short[neighbours]=arrive
                    queue.append([neighbours,arrive])
                elif short[neighbours]<arrive<long[neighbours]:
                    long[neighbours]=arrive
                    queue.append([neighbours,arrive])
       
        return long[n]

