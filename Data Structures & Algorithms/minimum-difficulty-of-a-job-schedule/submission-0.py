class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d>len(jobDifficulty):
            return -1
        cache={}
        def helper(i,m):
            if (i,m) in cache:
                return cache[(i,m)]
            if m==1:
                return max(jobDifficulty[i:])
            if i == len(jobDifficulty):
                return 0

            result=float('inf')
            currmax=0
            for j in range(i,len(jobDifficulty)-m+1):
                currmax=max(jobDifficulty[j],currmax)
                result=min(result,currmax+helper(j+1,m-1))
            cache[(i,m)]=result
            return result
        return helper(0,d)

        pass
