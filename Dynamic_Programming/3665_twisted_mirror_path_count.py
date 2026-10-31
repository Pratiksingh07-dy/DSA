class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # Where the robot ends after entering a mirror.
        # right_exit: entered mirror while moving right.
        # down_exit: entered mirror while moving down.
        right_exit = [[-1] * n for _ in range(m)]
        down_exit = [[-1] * n for _ in range(m)]

        # Precompute mirror chains in reverse order.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if grid[i][j] == 1:

                    # Entered while moving right -> reflected down.
                    if i + 1 < m:
                        if grid[i + 1][j] == 0:
                            right_exit[i][j] = i * n + j + n
                        else:
                            right_exit[i][j] = down_exit[i + 1][j]

                    # Entered while moving down -> reflected right.
                    if j + 1 < n:
                        if grid[i][j + 1] == 0:
                            down_exit[i][j] = i * n + j + 1
                        else:
                            down_exit[i][j] = right_exit[i][j + 1]

        # Standard path-counting DP.
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                ways = dp[i][j]

                # Move right.
                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        ni, nj = i, j + 1
                        dp[ni][nj] = (dp[ni][nj] + ways) % MOD
                    else:
                        dest = right_exit[i][j + 1]
                        if dest != -1:
                            ni, nj = divmod(dest, n)
                            dp[ni][nj] = (dp[ni][nj] + ways) % MOD

                # Move down.
                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        ni, nj = i + 1, j
                        dp[ni][nj] = (dp[ni][nj] + ways) % MOD
                    else:
                        dest = down_exit[i + 1][j]
                        if dest != -1:
                            ni, nj = divmod(dest, n)
                            dp[ni][nj] = (dp[ni][nj] + ways) % MOD

        return dp[m - 1][n - 1]