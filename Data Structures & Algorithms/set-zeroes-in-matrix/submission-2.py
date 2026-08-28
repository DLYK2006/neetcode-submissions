class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        bruh=False
        for i in range(row):
            for m in range(col):
                if matrix[i][m]==0:
                    matrix[0][m]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        bruh=True

        for i in range(1,row):
            for m in range(1,col):
                if matrix[i][0]==0 or matrix[0][m]==0:
                    matrix[i][m]=0

        if matrix[0][0]==0:
            for i in range(row):
                matrix[i][0]=0
        
        if bruh:
            for i in range(col):
                matrix[0][i]=0