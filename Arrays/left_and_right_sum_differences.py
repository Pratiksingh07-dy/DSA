class Solution:
    def leftRightDifference(self, nums):

        total_sum = sum(nums)

        left_sum = 0

        answer = []

        for num in nums:

            total_sum -= num

            answer.append(
                abs(left_sum - total_sum)
            )

            left_sum += num

        return answer


# Test Code

nums = [10,4,8,3]

obj = Solution()

answer = obj.leftRightDifference(nums)

print(answer)


# -----------------------------
# Pattern Used: Prefix Sum
#
# Why:
# Need left sum and right sum
# for every index efficiently.
#
# My thinking:
# 1. Find total array sum
# 2. Keep track of left sum
# 3. Right sum =
#    total_sum - current element
# 4. Calculate difference
# 5. Store answer
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------