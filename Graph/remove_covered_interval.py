class Solution:

    def removeCoveredIntervals(
        self,
        intervals
    ):

        intervals.sort(
            key=lambda x: (
                x[0],
                -x[1]
            )
        )

        count = 0

        maxEnd = 0

        for start, end in intervals:

            if end > maxEnd:

                count += 1

                maxEnd = end

        return count


# -----------------------------
# Pattern Used:
#
# Greedy
#
# +
#
# Sorting
#
#
# Why:
#
# Sort by
#
# Start Ascending
#
# End Descending
#
# Then keep track of
# the largest end seen.
#
# If current interval
# ends before or at
# maxEnd,
# it is covered.
#
#
# My Thinking:
#
# 1. Sort intervals.
#
# 2. Maintain maximum
#    end seen.
#
# 3. If current end
#    <= maxEnd,
#    ignore it.
#
# 4. Otherwise,
#    keep it and
#    update maxEnd.
#
#
# Time Complexity:
#
# O(n log n)
#
# Space Complexity:
#
# O(1)
# (Ignoring sorting space)
# -----------------------------


intervals = [
    [1,4],
    [3,6],
    [2,8]
]

obj = Solution()

print(
    obj.removeCoveredIntervals(
        intervals
    )
)

# Output:
# 2