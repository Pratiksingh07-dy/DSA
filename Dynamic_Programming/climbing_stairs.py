class Solution:

    def climbStairs(
        self,
        n
    ):

        # Base cases

        if n <= 2:

            return n


        first = 1

        second = 2


        # Build answer

        for _ in range(

            3,

            n + 1

        ):

            current = (

                first

                +

                second

            )

            first = second

            second = current


        return second


# ----------------------------------
# Pattern Used:
#
# Dynamic Programming
#
# +
#
# Fibonacci
#
#
# My Thinking:
#
# To reach step n,
# we can come from:
#
# n-1
#
# or
#
# n-2
#
# Therefore:
#
# dp[n]
#
# =
#
# dp[n-1]
#
# +
#
# dp[n-2]
#
# Instead of storing
# the whole DP array,
# keep only the last
# two values.
#
#
# Time Complexity:
#
# O(n)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


n = 5


obj = Solution()

result = obj.climbStairs(

    n

)

print(result)

# Output:
# 8g