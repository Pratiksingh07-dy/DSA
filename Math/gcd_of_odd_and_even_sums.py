class Solution:

    def gcdOfOddEvenSums(
        self,
        n
    ):

        return n


# ----------------------------------
# Pattern Used:
#
# Math
#
#
# My Thinking:
#
# Sum of first n odd
# numbers = n²
#
# Sum of first n even
# numbers = n(n + 1)
#
# GCD:
#
# gcd(n², n(n + 1))
#
# = n * gcd(n, n + 1)
#
# Consecutive numbers
# always have GCD 1.
#
# Therefore answer = n.
#
#
# Time Complexity:
#
# O(1)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


n = 4

obj = Solution()

print(

    obj.gcdOfOddEvenSums(

        n

    )

)

# Output:
# 4