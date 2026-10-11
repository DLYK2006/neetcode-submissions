class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependancy={}
        for i in range(numCourses):
            dependancy[i]=[]
        for a,b in prerequisites:
            dependancy[a].append(b)
        
        visitted=set()
        done=set()
        def dfs(node):
            if node in done:
                return True
            if node in visitted:
                return False
            visitted.add(node)
            for i in dependancy[node]:
                if dfs(i) is False:
                    return False
            visitted.remove(node)
            done.add(node)
        
        for i in range(numCourses):
            if dfs(i) is False:
                return False
        return True