class Solution:

    def smallestPalindrome(
        self,
        s
    ):

        freq = [

            0

        ] * 26


        # Count frequency

        for ch in s:

            freq[

                ord(ch)

                -

                ord('a')

            ] += 1


        left = []

        middle = ""


        # Build first half

        for i in range(26):

            left.append(

                chr(

                    i + ord('a')

                )

                *

                (

                    freq[i] // 2

                )

            )


            if (

                freq[i] % 2

            ):

                middle = chr(

                    i + ord('a')

                )


        left = "".join(

            left

        )


        return (

            left

            +

            middle

            +

            left[::-1]

        )


# ----------------------------------
# Pattern Used:
#
# Arrays
#
# +
#
# Frequency Count
#
#
# My Thinking:
#
# 1. Count frequency
#    of every character.
#
# 2. Put half of each
#    character into
#    the left half.
#
# 3. If a character has
#    odd frequency,
#    keep one copy
#    as the middle.
#
# 4. Reverse the left
#    half to build
#    the right half.
#
# 5. Since we add
#    characters from
#    'a' to 'z',
#    the palindrome is
#    lexicographically
#    smallest.
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


s = "babab"

obj = Solution()

result = obj.smallestPalindrome(

    s

)

print(result)

# Output:
# abbba