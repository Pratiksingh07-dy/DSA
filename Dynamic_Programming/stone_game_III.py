class Solution:

    def stoneGameIII(
        self,
        stoneValue
    ):

        n = len(

            stoneValue

        )


        # dp[i]
        #
        # Maximum score
        # difference the
        # current player
        # can achieve
        # starting from i.

        dp = [

            0

        ] * (

            n + 1

        )


        # Build DP
        # from back

        for i in range(

            n - 1,

            -1,

            -1

        ):

            take = 0

            dp[i] = float(

                "-inf"

            )


            # Take
            # 1, 2 or 3
            # stones

            for j in range(

                i,

                min(

                    i + 3,

                    n

                )

            ):

                take += (

                    stoneValue[j]

                )


                dp[i] = max(

                    dp[i],

                    take

                    -

                    dp[j + 1]

                )


        if dp[0] > 0:

            return "Alice"

        elif dp[0] < 0:

            return "Bob"

        else:

            return "Tie"


# ----------------------------------
# Pattern Used:
#
# Dynamic Programming
#
# +
#
# Minimax
#
#
# My Thinking:
#
# dp[i]
#
# =
#
# Maximum score
# difference
# current player
# can achieve
# from index i.
#
# Current player
# can take:
#
# 1
#
# or
#
# 2
#
# or
#
# 3 stones.
#
# Opponent will
# also play
# optimally.
#
#
# Time Complexity:
#
# O(n)
#
#
# Space Complexity:
#
# O(n)
# ----------------------------------


stoneValue = [

    1,

    2,

    3,

    7

]


obj = Solution()

print(

    obj.stoneGameIII(

        stoneValue

    )

)

# Output:
# Bob