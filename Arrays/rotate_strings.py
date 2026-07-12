class Solution:

    def rotateString(
        self,
        s,
        goal
    ):

        if (

            len(s)

            !=

            len(goal)

        ):

            return False

        return (

            goal

            in

            (s + s)

        )


# ----------------------------------
# Pattern Used:
#
# Arrays
#
# +
#
# String Manipulation
#
#
# Why:
#
# If goal is a rotation
# of s, then it must
# appear inside
# s + s.
#
#
# My Thinking:
#
# 1. Lengths must be
#    equal.
#
# 2. Concatenate s
#    with itself.
#
# 3. Search goal in
#    the new string.
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


s = "abcde"

goal = "cdeab"

obj = Solution()

print(

    obj.rotateString(

        s,

        goal

    )

)

# Output:
# True