class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        k = len(word)
        directions = [(0,-1),(-1,0),(1,0),(0,1)]
        self.found = False
        
        def search(i, x, y):
            # print("i", i, "x", x, "y", y)
            if i == k:
                self.found = True
                return
            
            if board[x][y] == word[i]:
                board[x][y] = ""
                if i + 1 == k:
                    self.found = True
                    return                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        search(i+1, nx, ny)
                board[x][y] = word[i]
        
        for i in range(m):
            for j in range(n):
                if self.found:
                    return True
                search(0, i, j)

        return self.found
            