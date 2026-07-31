class Solution:

    def minimumPushes(
        self,
        word
    ):

        freq = [

            0

        ] * 26


        # Count frequency
        # of every letter.

        for ch in word:

            freq[

                ord(ch)

                -

                ord('a')

            ] += 1


        # Most frequent
        # letters first.

        freq.sort(

            reverse=True

        )


        answer = 0


        for i in range(

            26

        ):

            if (

                freq[i] == 0

            ):

                break


            answer += (

                freq[i]

                *

                (

                    (i // 8)

                    +

                    1

                )

            )


        return answer


# ----------------------------------
# Pattern Used:
#
# Greedy
#
# +
#
# Frequency Count
#
#
# My Thinking:
#
# The most frequent
# letters should cost
# the fewest pushes.
#
# Count frequency
# of every letter.
#
# Sort frequencies
# in decreasing order.
#
# First 8 letters:
# 1 push
#
# Next 8 letters:
# 2 pushes
#
# Next 8 letters:
# 3 pushes
#
# Remaining:
# 4 pushes.
#
#
# Time Complexity:
#
# O(n)
#
# (Sorting only
# 26 values)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


word = "aabbccddeeffgghhiiiiii"

obj = Solution()

result = obj.minimumPushes(

    word

)

print(result)

# Output:
# 24