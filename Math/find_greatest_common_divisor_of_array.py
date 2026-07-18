

from math import gcd


class Solution:

    def findGCD(
        self,
        nums
    ):

        smallest = min(nums)

        largest = max(nums)

        return gcd(

            smallest,

            largest

        )


# ----------------------------------
# Pattern Used:
#
# Math
#
#
# My Thinking:
#
# 1. Find the smallest
#    element.
#
# 2. Find the largest
#    element.
#
# 3. Calculate their GCD.
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


nums = [

    2,

    5,

    6,

    9,

    10

]

obj = Solution()

print(

    obj.findGCD(

        nums

    )

)

# Output:
# 2