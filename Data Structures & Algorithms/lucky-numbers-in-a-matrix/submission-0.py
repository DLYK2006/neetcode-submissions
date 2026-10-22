class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minimum=[]
        maximum=[]
        result=[]

        for i in range(len(matrix)):
            minimum.append(min(matrix[i]))
        
        for i in range(len(matrix[0])):
            arr=[]
            for m in range(len(matrix)):
                arr.append(matrix[m][i])
            maximum.append(max(arr))
        
        for i in range(len(minimum)):
            if minimum[i] in maximum:
                result.append(minimum[i])
        return result


        pass
