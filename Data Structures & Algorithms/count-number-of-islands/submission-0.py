from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        directions = [(0,-1),(-1,0),(1,0),(0,1)]
        m, n = len(grid), len(grid[0])
        
        def bfs(i, j):
            queue = deque()
            if grid[i][j] == "1":
                queue.append((i, j))
                grid[i][j] = "0"
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        queue.append((nx, ny))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        return ans
