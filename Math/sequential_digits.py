class Solution:

    def sequentialDigits(
        self,
        low,
        high
    ):

        digits = "123456789"

        answer = []

        lowLength = len(

            str(low)

        )

        highLength = len(

            str(high)

        )

        for length in range(

            lowLength,

            highLength + 1

        ):

            for start in range(

                10 - length

            ):

                number = int(

                    digits[
                        start:
                        start + length
                    ]

                )

                if (

                    low

                    <=

                    number

                    <=

                    high

                ):

                    answer.append(

                        number

                    )

        return answer


# ----------------------------------
# Pattern Used:
#
# Math
# +
# Simulation
#
#
# Why:
#
# All sequential numbers
# already exist inside
# "123456789".
#
# Just generate every
# possible substring.
#
#
# My Thinking:
#
# 1. Store
#    "123456789".
#
# 2. Generate every
#    substring whose
#    length matches
#    possible answers.
#
# 3. Convert it into
#    an integer.
#
# 4. Check whether it
#    lies inside
#    [low, high].
#
#
# Time Complexity:
#
# O(1)
#
# (At most 36 numbers
# are generated.)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


low = 100

high = 300

obj = Solution()

print(

    obj.sequentialDigits(

        low,

        high

    )

)

# Output:
# [123, 234]