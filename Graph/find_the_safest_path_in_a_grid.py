from collections import deque


class Solution:

    def maximumSafenessFactor(self, grid):

        n = len(grid)

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # Distance from nearest thief
        dist = [
            [-1] * n
            for _ in range(n)
        ]

        queue = deque()

        # Put all thieves into queue
        for i in range(n):

            for j in range(n):

                if grid[i][j] == 1:

                    dist[i][j] = 0

                    queue.append(
                        (i, j)
                    )

        # Multi Source BFS
        while queue:

            x, y = queue.popleft()

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                if (
                    0 <= nx < n and
                    0 <= ny < n and
                    dist[nx][ny] == -1
                ):

                    dist[nx][ny] = (
                        dist[x][y] + 1
                    )

                    queue.append(
                        (nx, ny)
                    )

        # Check if path exists
        def bfs(limit):

            if dist[0][0] < limit:

                return False

            visited = [
                [False] * n
                for _ in range(n)
            ]

            queue = deque()

            queue.append(
                (0, 0)
            )

            visited[0][0] = True

            while queue:

                x, y = queue.popleft()

                if (
                    x == n - 1 and
                    y == n - 1
                ):

                    return True

                for dx, dy in directions:

                    nx = x + dx
                    ny = y + dy

                    if (
                        0 <= nx < n and
                        0 <= ny < n and
                        not visited[nx][ny] and
                        dist[nx][ny] >= limit
                    ):

                        visited[nx][ny] = True

                        queue.append(
                            (nx, ny)
                        )

            return False

        left = 0

        right = max(
            max(row)
            for row in dist
        )

        answer = 0

        while left <= right:

            mid = (
                left + right
            ) // 2

            if bfs(mid):

                answer = mid

                left = mid + 1

            else:

                right = mid - 1

        return answer


# -----------------------------
# Pattern Used:
# Graph
#
# Why:
# Need the safest path.
# First calculate every
# cell's distance from the
# nearest thief.
# Then Binary Search the
# maximum safeness.
#
# My thinking:
#
# Step 1:
# Multi Source BFS
# from all thieves.
#
# Step 2:
# Build distance matrix.
#
# Step 3:
# Binary Search answer.
#
# Step 4:
# For every answer,
# run BFS.
#
# Step 5:
# If destination can be
# reached using only cells
# having distance >= answer,
# try larger answer.
#
# Example:
#
# Grid
#
# 0 0 1
# 0 0 0
# 0 0 0
#
# Distance Matrix
#
# 2 1 0
# 3 2 1
# 4 3 2
#
# Binary Search:
#
# Can travel using
# cells >=2 ?
#
# YES
#
# Try 3.
#
# If NO
#
# Answer =2
#
# Time Complexity:
#
# O(n² log n)
#
# Reason:
#
# Multi Source BFS
# + Binary Search
# + BFS validation.
#
# Space Complexity:
#
# O(n²)
# -----------------------------


# Test

grid = [
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0]
]

obj = Solution()

print(
    obj.maximumSafenessFactor(
        grid
    )
)

# Output:
# 2