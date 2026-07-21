class Solution:

    def maxActiveSectionsAfterTrade(
        self,
        s
    ):

        original = s.count('1')

        t = '1' + s + '1'

        groups = []

        i = 0

        while i < len(t):

            if t[i] == '0':

                j = i

                while (

                    j < len(t)

                    and

                    t[j] == '0'

                ):

                    j += 1

                groups.append(

                    j - i

                )

                i = j

            else:

                i += 1


        if len(groups) < 2:

            return original


        best = 0

        for i in range(

            len(groups) - 1

        ):

            best = max(

                best,

                groups[i]

                +

                groups[i + 1]

            )


        return original + best


# ----------------------------------
# Pattern Used:
#
# Arrays
#
# +
#
# Group Counting
#
#
# My Thinking:
#
# 1. Count original 1s.
#
# 2. Add "1" on both
#    sides of the string.
#
# 3. Find lengths of
#    all zero groups.
#
# 4. Take two consecutive
#    zero groups.
#
# 5. Their sum is the
#    possible gain.
#
# 6. Find maximum gain.
#
# 7. Add it to original
#    number of 1s.
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


s = "0100"

obj = Solution()

result = obj.maxActiveSectionsAfterTrade(

    s

)

print(result)