class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr):

        arr.sort()

        arr[0] = 1

        for i in range(1, len(arr)):

            arr[i] = min(
                arr[i],
                arr[i - 1] + 1
            )

        return arr[-1]


# Test

arr = [100,1,1000]

obj = Solution()

print(
    obj.maximumElementAfterDecrementingAndRearranging(arr)
)

# Output:
# 3


# -----------------------------
# Pattern Used:
# Greedy + Sorting
#
# Why:
# We can rearrange and
# decrease elements freely.
#
# My thinking:
# 1. Sort the array.
# 2. Make first element = 1.
# 3. Every next element can
#    be at most previous + 1.
# 4. If larger, decrease it.
# 5. Last element becomes
#    maximum possible answer.
#
# Example:
#
# arr =
# [100,1,1000]
#
# Sort:
#
# [1,100,1000]
#
# Make:
#
# [1,2,3]
#
# Answer = 3
#
# Time Complexity:
# O(n log n)
#
# Reason:
# Sorting dominates.
#
# Space Complexity:
# O(1)
# -----------------------------