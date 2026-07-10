

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()
        for a in range(len(grid)):
            for b in range(len(grid[a])):
                if grid[a][b]==0:
                    queue.append((a,b))
        
        while queue:
            a,b=queue.popleft()
            rows, cols = len(grid), len(grid[0])
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = a + dr, b + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[a][b] + 1
                    queue.append((nr, nc))
                    