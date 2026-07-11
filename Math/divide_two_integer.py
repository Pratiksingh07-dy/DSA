class Solution:

    def divide(
        self,
        dividend,
        divisor
    ):

        INT_MAX = (
            2 ** 31
        ) - 1

        INT_MIN = (
            -2 ** 31
        )

        if (
            dividend == INT_MIN
            and
            divisor == -1
        ):

            return INT_MAX

        negative = (

            (dividend < 0)

            !=

            (divisor < 0)

        )

        dividend = abs(
            dividend
        )

        divisor = abs(
            divisor
        )

        quotient = 0

        while (

            dividend
            >=
            divisor

        ):

            temp = divisor

            multiple = 1

            while (

                dividend
                >=
                (temp << 1)

            ):

                temp <<= 1

                multiple <<= 1

            dividend -= temp

            quotient += multiple

        if negative:

            quotient = -quotient

        return quotient


# ----------------------------------
# Pattern Used:
#
# Bit Manipulation
#
# +
#
# Bit Shifting
#
#
# Why:
#
# Instead of subtracting
# divisor one by one,
# double it using
# left shift.
#
# This reduces the
# number of operations.
#
#
# My Thinking:
#
# 1. Handle overflow.
#
# 2. Save sign.
#
# 3. Convert both
#    numbers to positive.
#
# 4. Keep doubling
#    divisor until it
#    cannot be doubled.
#
# 5. Subtract the
#    largest possible
#    multiple.
#
# 6. Repeat until
#    dividend becomes
#    smaller than divisor.
#
#
# Time Complexity:
#
# O((log N)^2)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


dividend = 10

divisor = 3

obj = Solution()

print(

    obj.divide(

        dividend,

        divisor

    )

)

# Output:
# 3