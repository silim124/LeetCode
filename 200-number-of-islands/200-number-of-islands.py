class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        
        def bfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r, c) in visited:
                return
            visited.add((r, c))
            for dir in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                bfs(r + dir[0], c + dir[1])
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
        bfs(0, 0)
        return res
        