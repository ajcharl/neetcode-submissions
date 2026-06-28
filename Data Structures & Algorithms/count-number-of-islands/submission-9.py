class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r, c):
            if (r < 0 # top
                or c < 0 # left
                or r >= rows # bottom
                or c >= cols # right
                or grid[r][c] == "0"
            ):
                return
            
            grid[r][c] = "0"

            dfs(r + 1, c) # down
            dfs(r - 1, c) # up
            dfs(r, c + 1) # right
            dfs(r, c - 1) # left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c)
        
        return island_count