class Solution:

    def separateDigits(self, nums):

        answer = []

        for num in nums:

            for digit in str(num):

                answer.append(int(digit))

        return answer


# Test Code

nums = [13,25,83,77]

obj = Solution()

answer = obj.separateDigits(nums)

print(answer)


# -----------------------------
# Pattern Used:
# Array + String Conversion
#
# Why:
# Need to separate digits
# from every number.
#
# My thinking:
# 1. Visit each number
# 2. Convert number to string
# 3. Visit each digit
# 4. Convert digit back to int
# 5. Add to answer array
#
# Example:
#
# 13 -> "13"
#
# '1' -> 1
# '3' -> 3
#
# Answer:
# [1,3]
#
# Time Complexity: O(total digits)
# Space Complexity: O(total digits)
# -----------------------------