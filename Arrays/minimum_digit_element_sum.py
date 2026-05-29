# 3300 Miinimum element after replacement with digit sum
 # adding all digits and then choosing ,inimum 

class Solution:
    def minElement(self, nums):

        minimum = float('inf')

        for num in nums:

            digit_sum = 0

            while num > 0:

                digit_sum += num % 10

                num //= 10

            minimum = min(minimum, digit_sum)

        return minimum


# Test Code
nums = [10,12,13,14]

obj = Solution()

answer = obj.minElement(nums)

print("Minimum Element:", answer)



# Pattern Used: Array Traversal
#
# Why:
# Need digit sum of every number
# and then find minimum.
#
# My thinking:
# 1. Traverse array
# 2. Calculate digit sum
# 3. Track smallest digit sum
# 4. Return minimum
#
# Time Complexity: O(n * d)