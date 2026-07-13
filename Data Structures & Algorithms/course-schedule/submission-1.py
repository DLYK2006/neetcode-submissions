class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph={}
        for i in range(numCourses):
            self.graph[i]=[]
        for a,b in prerequisites:
            self.graph[a].append(b)
        
        safe=set()
        for i in range(numCourses):
            path=set()
            if(self.dfs(i,path,safe) is False):
                return False
        return True

        
    
    def dfs(self,course,path,safe):
        if course in path:
            return False
        if course in safe:
            return True

        path.add(course)
        for a in self.graph[course]:
            if self.dfs(a,path,safe) is False:
                return False
        path.remove(course)
        safe.add(course)
        return True
