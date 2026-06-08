class Solution:
    def pivotArray(self, nums, pivot):

        smaller = []

        equal = []

        greater = []

        for num in nums:

            if num < pivot:
                smaller.append(num)

            elif num == pivot:
                equal.append(num)

            else:
                greater.append(num)

        return smaller + equal + greater


# Test Code

nums = [9,12,5,10,14,3,10]
pivot = 10

obj = Solution()

answer = obj.pivotArray(nums, pivot)

print(answer)


# -----------------------------
# Pattern Used: Array Traversal
#
# Why:
# Need to place:
# smaller elements first,
# then pivot elements,
# then greater elements.
#
# My thinking:
# 1. Create three arrays
# 2. Store elements < pivot
# 3. Store elements = pivot
# 4. Store elements > pivot
# 5. Join all arrays
#
# Example:
# nums = [9,12,5,10,14,3,10]
# pivot = 10
#
# smaller = [9,5,3]
# equal   = [10,10]
# greater = [12,14]
#
# answer =
# [9,5,3,10,10,12,14]
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------