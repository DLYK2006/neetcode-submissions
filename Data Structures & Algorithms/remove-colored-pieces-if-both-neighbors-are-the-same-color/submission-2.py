class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        acounts=0
        bcounts=0

        for i in range(1,len(colors)-1):
            if colors[i+1]=='A' and colors[i]=='A' and colors[i-1]=='A':
                acounts+=1
            elif colors[i+1]=='B' and colors[i]=='B' and colors[i-1]=='B':
                bcounts+=1
        
        if acounts>bcounts:
            return True
        else:
            return False
        pass
