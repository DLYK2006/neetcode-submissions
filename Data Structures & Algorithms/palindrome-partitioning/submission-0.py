class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result=[]
        self.s=s
        path=[]
        start=0
        self.helper(path,start)
        return self.result

    def helper(self,path,start):

        if start==len(self.s):
            self.result.append(path.copy())
            return path
        
        for end in range(start,len(self.s)):
            if self.s[start:end+1]==self.s[start:end+1][::-1]:
                path.append(self.s[start:end+1])
                self.helper(path,end+1)
                path.pop()