class Solution:

    def convert(
        self,
        s,
        numRows
    ):

        if (
            numRows == 1
            or
            numRows >= len(s)
        ):

            return s

        rows = [
            ""
        ] * numRows

        currentRow = 0

        direction = 1

        for ch in s:

            rows[currentRow] += ch

            if currentRow == 0:

                direction = 1

            elif currentRow == numRows - 1:

                direction = -1

            currentRow += direction

        return "".join(rows)


# -----------------------------
# Pattern Used:
#
# String
#
# +
#
# Simulation
#
#
# Why:
#
# Simulate writing
# characters row by row
# in a zigzag pattern.
#
#
# My Thinking:
#
# 1. Create one string
#    for each row.
#
# 2. Move downward.
#
# 3. When bottom is
#    reached,
#    move upward.
#
# 4. When top is
#    reached,
#    move downward.
#
# 5. Join all rows.
#
#
# Time Complexity:
#
# O(n)
#
#
# Space Complexity:
#
# O(n)
# -----------------------------


s = "PAYPALISHIRING"

numRows = 3

obj = Solution()

print(
    obj.convert(
        s,
        numRows
    )
)

# Output:
# PAHNAPLSIIGYIR