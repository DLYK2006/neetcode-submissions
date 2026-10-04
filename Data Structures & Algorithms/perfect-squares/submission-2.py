from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        
        squares=[]
        visited={n}
        for i in range(1,n+1):
            if i*i<=n:
                squares.append(i*i)
            else:
                break
        
        queue=deque([(n,0)])

        while queue:
            current,level=queue.popleft()
            for i in squares:
                new=current-i

                if new==0:
                    return level+1
                elif new<0:
                    break
                elif new not in visited:
                    visited.add(new)
                    queue.append((new,level+1))

                
