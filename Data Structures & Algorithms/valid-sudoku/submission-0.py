class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row=Solution.checkRow(board)
        column=Solution.checkColumn(board)
        box=Solution.checkBox(board)

        if(row==True & column==True & box==True):
            return True
        else:
            return False

    def checkRow(board: List[List[str]]) -> bool:

        for n in range(len(board)):
            seenRow=set()
            for i in range(len(board)):
                if(board[n][i]=="."):
                    continue
                elif(board[n][i] not in seenRow):
                    seenRow.add(board[n][i])
                else:
                    return False
        return True


    def checkColumn(board: List[List[str]]) -> bool:
        for n in range(len(board)):
            seenColumn=set()
            for i in range(len(board)):
                if(board[i][n]=="."):
                    continue
                elif(board[i][n] not in seenColumn):
                    seenColumn.add(board[i][n])
                else:
                    return False
        return True
    
    def checkBox(board: List[List[str]]) -> bool:
        for row in range(0,9,3):
            for column in range(0,9,3):
                seenBox=set()
                for r in range(row,row+3):
                    for c in range(column,column+3):
                        if(board[r][c]=="."):
                            continue
                        elif(board[r][c] not in seenBox):
                            seenBox.add(board[r][c])
                        else:
                            return False
        return True
                            
