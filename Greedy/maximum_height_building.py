class Solution:

    def maxBuilding(self, n, restrictions):

        restrictions.append([1, 0])

        restrictions.sort()

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        m = len(restrictions)

        # Left to Right Pass
        for i in range(1, m):

            dist = restrictions[i][0] - restrictions[i - 1][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + dist
            )

        # Right to Left Pass
        for i in range(m - 2, -1, -1):

            dist = restrictions[i + 1][0] - restrictions[i][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + dist
            )

        answer = 0

        for i in range(1, m):

            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            dist = x2 - x1

            peak = (h1 + h2 + dist) // 2

            answer = max(answer, peak)

        return answer


# Test

n = 5
restrictions = [[2,1],[4,1]]

obj = Solution()

print(
    obj.maxBuilding(
        n,
        restrictions
    )
)

# Output:
# 2


# -----------------------------
# Pattern Used:
# Greedy + Math
#
# Why:
# Restrictions affect nearby
# buildings because adjacent
# heights differ by at most 1.
#
# My thinking:
# 1. Add building 1 with
#    height 0.
# 2. Sort restrictions.
# 3. Propagate limits
#    left → right.
# 4. Propagate limits
#    right → left.
# 5. Find highest peak
#    possible between every
#    pair of restrictions.
#
# Example:
#
# n = 5
#
# restrictions:
# [2,1]
# [4,1]
#
# heights:
# [0,1,2,1,2]
#
# Answer = 2
#
# Time Complexity:
# O(m log m)
#
# Space Complexity:
# O(1)
#
# m = number of restrictions
# -----------------------------