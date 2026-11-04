class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sunMat=[]
        grah=[]
        for i in range(len(matrix)+1):
            grah=[]
            for m in range(len(matrix[0])+1):
                grah.append(0)
            self.sunMat.append(grah)
        
        for i in range(len(matrix)):
            pre=0
            for m in range(len(matrix[0])):
                pre+=matrix[i][m]
                above=self.sunMat[i][m+1]
                self.sunMat[i+1][m+1]=pre+above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight=self.sunMat[row2+1][col2+1]
        above=self.sunMat[row1][col2+1]
        left=self.sunMat[row2+1][col1]
        topLeft=self.sunMat[row1][col1]
        answer=bottomRight-above-left+topLeft
        return answer

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)