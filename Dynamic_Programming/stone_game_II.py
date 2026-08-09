from functools import lru_cache


class Solution:

    def stoneGameII(
        self,
        piles
    ):

        n = len(piles)

        # suffix[i] =
        # total stones from
        # i to the end

        suffix = [0] * (n + 1)

        for i in range(
            n - 1,
            -1,
            -1
        ):

            suffix[i] = (
                suffix[i + 1]
                +
                piles[i]
            )


        @lru_cache(None)
        def dp(
            i,
            M
        ):

            # No piles remaining

            if i >= n:

                return 0


            # Alice can take
            # all remaining piles

            if i + 2 * M >= n:

                return suffix[i]


            best = 0


            # Try every possible
            # X from 1 to 2M

            for X in range(

                1,

                2 * M + 1

            ):

                nextM = max(

                    M,

                    X

                )


                # Stones opponent
                # can eventually get

                opponent = dp(

                    i + X,

                    nextM

                )


                # Total remaining
                # stones - opponent's
                # best score

                current = (

                    suffix[i]

                    -

                    opponent

                )


                best = max(

                    best,

                    current

                )


            return best


        return dp(

            0,

            1

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
# Suffix Sum
#
#
# State:
#
# dp(i, M)
#
# = maximum stones
#   current player can get
#   starting from index i
#   with current M.
#
#
# Time Complexity:
#
# O(n^3)
#
#
# Space Complexity:
#
# O(n^2)
# ----------------------------------


piles = [

    2,

    7,

    9,

    4,

    4

]


obj = Solution()

print(

    obj.stoneGameII(

        piles

    )

)

# Output:
# 10