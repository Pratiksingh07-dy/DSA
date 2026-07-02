from heapq import heappush, heappop


class Solution:

    def findSafeWalk(self, grid, health):

        rows = len(grid)

        cols = len(grid[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # Distance stores
        # minimum damage taken
        dist = [
            [float("inf")] * cols
            for _ in range(rows)
        ]

        dist[0][0] = grid[0][0]

        heap = []

        heappush(
            heap,
            (
                grid[0][0],
                0,
                0
            )
        )

        while heap:

            damage, x, y = heappop(heap)

            if damage > dist[x][y]:

                continue

            if (
                x == rows - 1 and
                y == cols - 1
            ):

                break

            for dx, dy in directions:

                nx = x + dx

                ny = y + dy

                if (
                    0 <= nx < rows and
                    0 <= ny < cols
                ):

                    newDamage = (
                        damage +
                        grid[nx][ny]
                    )

                    if (
                        newDamage <
                        dist[nx][ny]
                    ):

                        dist[nx][ny] = newDamage

                        heappush(
                            heap,
                            (
                                newDamage,
                                nx,
                                ny
                            )
                        )

        return (
            dist[rows - 1][cols - 1]
            < health
        )


# -----------------------------
# Pattern Used:
#
# Graph
#
# Why:
#
# Every move has a cost.
#
# Safe cell = 0 damage
#
# Unsafe cell = +1 damage
#
# Need path with
# minimum damage.
#
# My thinking:
#
# 1. Treat every unsafe
#    cell as weight = 1.
#
# 2. Safe cell has
#    weight = 0.
#
# 3. Find path having
#    minimum damage.
#
# 4. If damage taken
#    is less than health,
#    answer is True.
#
# Example:
#
# 0 1 0
#
# 0 1 0
#
# 0 0 0
#
# Best path damage =1
#
# Health =2
#
# Remaining =1
#
# Reach destination
#
# Answer=True
#
# Time Complexity:
#
# O(mn log(mn))
#
# Reason:
#
# Dijkstra on
# m*n nodes.
#
# Space Complexity:
#
# O(mn)
# -----------------------------


# Test

grid = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0]
]

health = 1

obj = Solution()

print(
    obj.findSafeWalk(
        grid,
        health
    )
)

# Output:
# True