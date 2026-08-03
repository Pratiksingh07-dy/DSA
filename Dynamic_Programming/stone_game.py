class Solution:

    def stoneGame(
        self,
        piles
    ):

        return True


# ----------------------------------
# Pattern Used:
#
# Dynamic Programming
#
# (Mathematical Observation)
#
#
# My Thinking:
#
# Alice always wins.
#
# There are:
#
# - Even number of piles.
#
# - Total stones are odd.
#
# Alice can choose
# either all even-indexed
# piles or all odd-indexed
# piles.
#
# Before the game,
# she compares:
#
# Sum(Even)
#
# and
#
# Sum(Odd)
#
# She always chooses
# the larger one.
#
# Therefore,
# Alice is guaranteed
# to win.
#
#
# Time Complexity:
#
# O(1)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


piles = [

    5,

    3,

    4,

    5

]


obj = Solution()

print(

    obj.stoneGame(

        piles

    )

)

# Output:
# True