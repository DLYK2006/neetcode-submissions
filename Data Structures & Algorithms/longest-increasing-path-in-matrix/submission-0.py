class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache={}

        def helper(i,j):

            if (i,j) in cache:
                return cache[(i,j)]           

            result=1
            directions=[(0,1),(1,0),(-1,0),(0,-1)]
            for nr,nc in directions:
                dr,dc=nr+i,nc+j
                if dr==len(matrix) or dc==len(matrix[i]) or dr<0 or dc<0:
                    continue
                else:
                    if matrix[dr][dc]>matrix[i][j]:
                        result=max(result,helper(dr,dc)+1)

            cache[(i,j)]=result
            return cache[(i,j)]

        biggest=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                biggest=max(biggest,helper(i,j))
        
        return biggest
