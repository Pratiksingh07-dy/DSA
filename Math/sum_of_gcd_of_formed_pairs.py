from math import gcd


class Solution:

    def sumGCD(
        self,
        nums
    ):

        prefixGcd = []

        currentMax = 0

        # Create prefixGcd array

        for num in nums:

            currentMax = max(

                currentMax,

                num

            )

            prefixGcd.append(

                gcd(

                    num,

                    currentMax

                )

            )

        # Sort the array

        prefixGcd.sort()

        # Two pointers

        left = 0

        right = len(

            prefixGcd

        ) - 1

        answer = 0

        # Pair smallest
        # with largest

        while left < right:

            answer += gcd(

                prefixGcd[left],

                prefixGcd[right]

            )

            left += 1

            right -= 1

        return answer


# ----------------------------------
# Pattern Used:
#
# Math
#
# +
#
# Two Pointers
#
#
# My Thinking:
#
# 1. Keep track of
#    prefix maximum.
#
# 2. Calculate:
#
#    gcd(current number,
#        prefix maximum)
#
# 3. Store all results.
#
# 4. Sort them.
#
# 5. Use two pointers
#    to pair:
#
#    smallest + largest
#
# 6. Add the GCD
#    of every pair.
#
#
# Time Complexity:
#
# O(n log n)
#
#
# Space Complexity:
#
# O(n)
# ----------------------------------


nums = [

    3,

    6,

    2,

    8

]

obj = Solution()

print(

    obj.sumGCD(

        nums

    )

)

# Output:
# 5