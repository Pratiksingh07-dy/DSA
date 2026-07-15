class Solution:

    def furthestDistanceFromOrigin(
        self,
        moves
    ):

        left = moves.count('L')

        right = moves.count('R')

        blank = moves.count('_')

        return (

            abs(left - right)

            +

            blank

        )


# ----------------------------------
# Pattern Used:
#
# Greedy
#
#
# My Thinking:
#
# First calculate the
# current distance using:
#
# abs(left - right)
#
# Every "_" can move
# in whichever direction
# takes us further away.
#
# Therefore every "_"
# increases the maximum
# distance by 1.
#
#
# Formula:
#
# abs(L - R) + _
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


moves = "L_RL__R"

obj = Solution()

print(

    obj.furthestDistanceFromOrigin(

        moves

    )

)

# Output:
# 3