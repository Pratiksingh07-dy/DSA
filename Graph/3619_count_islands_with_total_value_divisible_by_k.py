
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                stack = [(r, c)]
                total = 0

                # Mark visited when adding to stack
                grid[r][c] = -grid[r][c]

                while stack:
                    x, y = stack.pop()
                    value = -grid[x][y]
                    total += value
                    grid[x][y] = 0

                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                            grid[nx][ny] = -grid[nx][ny]
                            stack.append((nx, ny))

                if total % k == 0:
                    count += 1

        return count
