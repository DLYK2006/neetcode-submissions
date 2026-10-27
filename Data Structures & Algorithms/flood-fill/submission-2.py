class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        queue = deque()
        queue.append((sr, sc))
        original=image[sr][sc]

        if image[sr][sc]==color:
            return image
        else:
            image[sr][sc]=color

        while queue:
            r, c = queue.popleft()
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0<=nr<len(image) and 0<=nc<len(image[0]) and image[nr][nc]==original:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        
        return image
