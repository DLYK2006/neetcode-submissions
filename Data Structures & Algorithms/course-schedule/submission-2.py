class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph={}
        self.seen=set()
        self.seeing=set()
        for i in range(numCourses):
            self.graph[i]=[]
        for a,b in prerequisites:
            self.graph[a].append(b)

        for i in range(numCourses):
            if self.dfs(i) is False:
                return False
        return True


    def dfs(self,node):
        if node in self.seeing:
            return False
        elif node in self.seen:
            return True
        self.seeing.add(node)
        for neighbor in self.graph[node]:
            if self.dfs(neighbor) is False:
                return False
        self.seeing.discard(node)
        self.seen.add(node)
            