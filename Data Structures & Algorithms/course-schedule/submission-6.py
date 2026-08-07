class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={}
        for i in range(numCourses):
            graph[i]=[]
        for a,b in prerequisites:
            graph[a].append(b)
        seen=set()
        safe=set()
        def dfs(course):
            if course in seen:
                return False
            if course in safe:
                return True
            seen.add(course)
            for i in graph[course]:
                if dfs(i) is False:
                    return False
            seen.remove(course)
            safe.add(course)
            return True
        for i in range(numCourses):
            if dfs(i) is False:
                return False
        return True