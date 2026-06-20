# 3300 Miinimum element after replacement with  sum
 # adding all s and then choosing ,inimum 

class Solution:
    def minElement(self, nums):

        minimum = float('inf')

        for num in nums:

            _sum = 0

            while num > 0:

                _sum += num % 10

                num //= 10

            minimum = min(minimum, _sum)

        return minimum


# Test Code
nums = [10,12,13,14]

obj = Solution()

answer = obj.minElement(nums)

print("Minimum Element:", answer)



# Pattern Used: Array Traversal
#
# Why:
# Need  sum of every number
# and then find minimum.
#
# My thinking:
# 1. Traverse array
# 2. Calculate  sum
# 3. Track smallest  sum
# 4. Return minimum
#
# Time Complexity: O(n * d)