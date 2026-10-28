
from typing import List

class Solution:
    def uniquePathGrid(self, m: int, n: int) -> List[str]:
        grid = [['#'] * n for _ in range(m)]

        # Create one guaranteed path:
        # Move right along the first row, then down the last column.
        for j in range(n):
            grid[0][j] = '.'

        for i in range(m):
            grid[i][n - 1] = '.'

        return [''.join(row) for row in grid]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathGrid(2, 3))
    print(sol.uniquePathGrid(3, 3))
    print(sol.uniquePathGrid(1, 4))
g