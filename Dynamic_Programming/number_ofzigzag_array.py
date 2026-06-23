class Solution:

    def zigZagArrays(self, n, l, r):

        MOD = 10**9 + 7

        m = r - l + 1

        up = [0] * m
        down = [0] * m

        # Length = 2 initialization
        for y in range(m):

            up[y] = y

            down[y] = m - y - 1

        if n == 2:

            return (
                sum(up) +
                sum(down)
            ) % MOD

        for _ in range(3, n + 1):

            prefUp = [0] * (m + 1)
            prefDown = [0] * (m + 1)

            for i in range(m):

                prefUp[i + 1] = (
                    prefUp[i] +
                    up[i]
                ) % MOD

                prefDown[i + 1] = (
                    prefDown[i] +
                    down[i]
                ) % MOD

            newUp = [0] * m
            newDown = [0] * m

            totalUp = prefUp[m]

            for y in range(m):

                # Previous move was DOWN
                # Now must go UP

                newUp[y] = prefDown[y]

                # Previous move was UP
                # Now must go DOWN

                newDown[y] = (
                    totalUp -
                    prefUp[y + 1]
                ) % MOD

            up = newUp
            down = newDown

        return (
            sum(up) +
            sum(down)
        ) % MOD


# -----------------------------
# Pattern Used:
# Dynamic Programming
# + Prefix Sum Optimization
#
# Why:
# Need to count number of
# valid ZigZag arrays.
#
# My thinking:
# 1. Track last direction.
# 2. up[y] =
#    arrays ending at y
#    where last move was UP.
#
# 3. down[y] =
#    arrays ending at y
#    where last move was DOWN.
#
# 4. To go UP:
#    previous value must
#    be smaller.
#
# 5. To go DOWN:
#    previous value must
#    be larger.
#
# 6. Use prefix sums to
#    avoid O(m²) transitions.
#
# Example:
#
# n = 3
# l = 1
# r = 3
#
# Valid:
#
# 1 2 1
# 1 3 1
# 1 3 2
#
# 2 1 2
# 2 1 3
# 2 3 1
# 2 3 2
#
# 3 1 2
# 3 1 3
# 3 2 3
#
# Answer = 10
#
# Time Complexity:
# O(n × m)
#
# m = r - l + 1
#
# Space Complexity:
# O(m)
# -----------------------------


# Test

n = 3
l = 1
r = 3

obj = Solution()

print(
    obj.zigZagArrays(
        n,
        l,
        r
    )
)

# Output:
# 10