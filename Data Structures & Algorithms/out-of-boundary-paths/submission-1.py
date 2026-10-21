class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache={}

        def helper(x,y,move):
            if (x,y,move) in cache:
                return cache[(x,y,move)]
            if (x==m or x<0) or (y==n or y<0):
                return 1
            if move==maxMove:
                return 0

            result=0
            up=helper(x-1,y,move+1)
            down=helper(x+1,y,move+1)
            left=helper(x,y-1,move+1)
            right=helper(x,y+1,move+1)

            result=(up+down+left+right)%1000000007
            cache[(x,y,move)]=result
            return result
        
        return helper(startRow,startColumn,0)
            


        pass
