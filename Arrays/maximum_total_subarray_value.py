class Solution:
    def maxTotalValue(self, nums, k):

        return (max(nums) - min(nums)) * k


# Test Code

nums = [4,2,5,1]
k = 3

obj = Solution()

answer = obj.maxTotalValue(nums, k)

print(answer)


# -----------------------------
# Pattern Used: Array Traversal
#
# Why:
# Same subarray can be chosen
# multiple times.
#
# My thinking:
# 1. Find maximum element
# 2. Find minimum element
# 3. Maximum subarray value is:
#    max(nums) - min(nums)
# 4. Choose that subarray
#    k times
# 5. Return:
#    (max-min) * k
#
# Example:
# nums = [4,2,5,1]
#
# max = 5
# min = 1
#
# value = 4
#
# k = 3
#
# answer = 4 * 3 = 12
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------