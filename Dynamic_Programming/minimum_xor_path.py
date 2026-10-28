
from typing import List

class Solution:
    def minPathXor(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]

                if i > 0:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ value)

                if j > 0:
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ value)

        return min(dp[m - 1][n - 1])


if __name__ == "__main__":
    sol = Solution()

    print(sol.minPathXor([[1, 2], [3, 4]]))  # 6
    print(sol.minPathXor([[6, 7], [5, 8]]))  # 9
    print(sol.minPathXor([[2, 7, 5]]))       # 0
