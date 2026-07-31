class Solution:

    def minimumPushes(
        self,
        word
    ):

        answer = 0


        # First 8 letters
        # cost 1 push.
        #
        # Next 8 letters
        # cost 2 pushes.
        #
        # Next 8 letters
        # cost 3 pushes.
        #
        # Remaining
        # cost 4 pushes.

        for i in range(

            len(word)

        ):

            answer += (

                i // 8

            ) + 1


        return answer


# ----------------------------------
# Pattern Used:
#
# Greedy
#
#
# My Thinking:
#
# There are only
# 8 keys:
#
# 2 to 9.
#
# So,
#
# First 8 letters
# should require
# only 1 push.
#
# Next 8 letters
# require 2 pushes.
#
# Next 8 letters
# require 3 pushes.
#
# Remaining letters
# require 4 pushes.
#
# Since all letters
# are distinct,
# only the number
# of letters matters.
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


word = "xycdefghij"

obj = Solution()

result = obj.minimumPushes(

    word

)

print(result)

# Output:
# 12