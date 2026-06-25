class Solution:

    def countSubarrays(self, nums, target):

        n = len(nums)

        answer = 0

        for left in range(n):

            target_count = 0

            for right in range(left, n):

                if nums[right] == target:

                    target_count += 1

                length = right - left + 1

                if target_count * 2 > length:

                    answer += 1

        return answer


# Test

nums = [1,2,2,3]
target = 2

obj = Solution()

print(
    obj.countSubarrays(
        nums,
        target
    )
)

# Output:
# 5


# -----------------------------
# Pattern Used:
# Prefix Sum / Running Count
#
# Why:
# Need to check every
# subarray while keeping
# count of target.
#
# My thinking:
# 1. Fix left boundary.
# 2. Extend right boundary.
# 3. Maintain frequency of target.
# 4. Check if target is
#    majority.
#
# Majority Condition:
#
# target_count >
# subarray_length / 2
#
# Example:
#
# nums =
# [1,2,2,3]
#
# target = 2
#
# Valid:
#
# [2]
# [2]
# [2,2]
# [1,2,2]
# [2,2,3]
#
# Answer = 5
#
# Time Complexity:
# O(n²)
#
# Space Complexity:
# O(1)
# -----------------------------