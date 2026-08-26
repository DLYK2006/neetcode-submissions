class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for m in range(i,len(matrix[i])):
                matrix[i][m],matrix[m][i]=matrix[m][i],matrix[i][m]
        print()