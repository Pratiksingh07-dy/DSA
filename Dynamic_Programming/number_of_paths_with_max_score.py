class Solution:

    def pathsWithMaxScore(
        self,
        board
    ):

        MOD = 10 ** 9 + 7

        n = len(board)

        score = [
            [-1] * n
            for _ in range(n)
        ]

        ways = [
            [0] * n
            for _ in range(n)
        ]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in range(
            n - 1,
            -1,
            -1
        ):

            for j in range(
                n - 1,
                -1,
                -1
            ):

                if board[i][j] == "X":

                    continue

                if (
                    i == n - 1
                    and
                    j == n - 1
                ):

                    continue

                best = -1
                count = 0

                for x, y in [

                    (i + 1, j),

                    (i, j + 1),

                    (i + 1, j + 1)

                ]:

                    if (
                        x < n
                        and
                        y < n
                        and
                        score[x][y] != -1
                    ):

                        if score[x][y] > best:

                            best = score[x][y]

                            count = ways[x][y]

                        elif score[x][y] == best:

                            count = (
                                count
                                +
                                ways[x][y]
                            ) % MOD

                if best == -1:

                    continue

                value = 0

                if board[i][j].isdigit():

                    value = int(
                        board[i][j]
                    )

                score[i][j] = (
                    best + value
                )

                ways[i][j] = count

        if ways[0][0] == 0:

            return [
                0,
                0
            ]

        return [
            score[0][0],
            ways[0][0]
        ]


# ---------------------------------
# Pattern Used:
#
# Dynamic Programming
#
# Grid DP
#
#
# Why?
#
# Need
#
# 1. Maximum Score
#
# 2. Number of paths
#
# simultaneously.
#
#
# DP State:
#
# score[i][j]
#
# =
#
# Maximum score
# from (i,j)
# to S.
#
#
# ways[i][j]
#
# =
#
# Number of paths
# giving that score.
#
#
# Transition:
#
# Look at
#
# Down
#
# Right
#
# Diagonal
#
# because we are
# filling table
# backwards.
#
#
# Time Complexity:
#
# O(n²)
#
#
# Space Complexity:
#
# O(n²)
# ---------------------------------


board = [

    "E23",

    "2X2",

    "12S"

]

obj = Solution()

print(
    obj.pathsWithMaxScore(
        board
    )
)

# Output
# [7, 1]