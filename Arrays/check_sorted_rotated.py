class Solution:
    def check(self, nums):

        count = 0
        n = len(nums)

        for i in range(n):

            if nums[i] > nums[(i+1)%n]:
                count += 1

        return count <= 1


# Test Code
nums = [3,4,5,1,2]

obj = Solution()

answer = obj.check(nums)

print("Is Sorted and Rotated:", answer)


# -----------------------------
# Pattern Used: Array Traversal
#
# Why:
# Need to count how many times
# sorted order breaks.
#
# My thinking:
# 1. Traverse whole array
# 2. Compare current with next
# 3. Count decreasing points
# 4. Valid array can break only once
#