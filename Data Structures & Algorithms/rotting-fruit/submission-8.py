from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0

        minutes_elapsed = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c, minutes = queue.popleft()
            minutes_elapsed = minutes

            for dr, dc in directions:
                neighbor_r, neighbor_c = r + dr, c + dc

                if (
                    0 <= neighbor_r < rows
                    and 0 <= neighbor_c < cols
                    and grid[neighbor_r][neighbor_c] == 1
                ):
                    grid[neighbor_r][neighbor_c] = 2
                    fresh_oranges -= 1

                    queue.append((neighbor_r, neighbor_c, minutes + 1))
        return minutes_elapsed if fresh_oranges == 0 else -1