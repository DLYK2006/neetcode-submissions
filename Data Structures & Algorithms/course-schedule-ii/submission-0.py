class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph={}
        result=[]
        queue=deque()
        for a in range(numCourses):
            self.graph[a]=[]
        for a,b in prerequisites:
            self.graph[a].append(b)
        
        for i in range(len(self.graph)):
            if(len(self.graph[i]))==0:
                queue.append(i)
        
        while queue:
            grah=queue.popleft()
            result.append(grah)
            for i in range(len(self.graph)):
                if grah in self.graph[i]:
                    self.graph[i].remove(grah)
                    if len(self.graph[i])==0:
                        queue.append(i)

        if len(result)==numCourses:
            return result
        else:
            return []

