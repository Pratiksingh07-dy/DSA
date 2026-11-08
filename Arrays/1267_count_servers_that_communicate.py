from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_count = [0] * m
        col_count = [0] * n

        # Count servers in every row and column.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Count servers that share a row or column with another server.
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    grid = [
        [1, 0],
        [1, 1]
    ]

    print(sol.countServers(grid))