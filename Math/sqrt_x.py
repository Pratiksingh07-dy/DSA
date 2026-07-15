class Solution:

    def mySqrt(
        self,
        x
    ):

        if x < 2:

            return x

        left = 1

        right = x // 2

        answer = 0

        while left <= right:

            mid = (

                left + right

            ) // 2

            if mid * mid <= x:

                answer = mid

                left = mid + 1

            else:

                right = mid - 1

        return answer


# ----------------------------------
# Pattern Used:
#
# Binary Search
#
#
# My Thinking:
#
# Search for the largest
# number whose square
# is <= x.
#
# If mid² <= x:
# mid can be the answer,
# but search further right.
#
# If mid² > x:
# mid is too large,
# so search left.
#
#
# Time Complexity:
#
# O(log x)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


x = 8

obj = Solution()

print(

    obj.mySqrt(

        x

    )

)

# Output:
# 2