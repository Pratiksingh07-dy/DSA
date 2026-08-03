from functools import lru_cache


class Solution:

    def PredictTheWinner(
        self,
        nums
    ):

        @lru_cache(None)

        def dp(

            left,

            right

        ):

            # Only one number left

            if left == right:

                return nums[left]


            # Pick left number

            pickLeft = (

                nums[left]

                -

                dp(

                    left + 1,

                    right

                )

            )


            # Pick right number

            pickRight = (

                nums[right]

                -

                dp(

                    left,

                    right - 1

                )

            )


            # Current player
            # wants maximum
            # score difference

            return max(

                pickLeft,

                pickRight

            )


        return (

            dp(

                0,

                len(nums) - 1

            )

            >= 0

        )


# ----------------------------------
# Pattern Used:
#
# Dynamic Programming
#
# +
#
# Minimax
#
# +
#
# Memoization
#
#
# My Thinking:
#
# dp(l, r)
#
# =
#
# Maximum score
# difference
# current player
# can achieve
# from nums[l...r].
#
# Either:
#
# Pick left
#
# or
#
# Pick right.
#
# Opponent will
# also play
# optimally.
#
#
# Time Complexity:
#
# O(n²)
#
#
# Space Complexity:
#
# O(n²)
# ----------------------------------


nums = [

    1,

    5,

    233,

    7

]


obj = Solution()

print(

    obj.PredictTheWinner(

        nums

    )

)

# Output:
# True