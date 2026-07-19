class Solution:

    def smallestSubsequence(
        self,
        s
    ):

        last = {}

        for i, char in enumerate(s):

            last[char] = i


        stack = []

        seen = set()


        for i, char in enumerate(s):

            if char in seen:

                continue


            while (

                stack

                and

                char < stack[-1]

                and

                last[stack[-1]] > i

            ):

                removed = stack.pop()

                seen.remove(

                    removed

                )


            stack.append(

                char

            )

            seen.add(

                char

            )


        return "".join(

            stack

        )


# ----------------------------------
# Pattern Used:
#
# Monotonic Stack
#
# +
#
# Greedy
#
#
# My Thinking:
#
# 1. Store the last
#    position of every
#    character.
#
# 2. Skip characters
#    already in stack.
#
# 3. If current character
#    is smaller than the
#    stack top, remove the
#    top ONLY if it appears
#    again later.
#
# 4. Add current character.
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
# Only 26 lowercase letters.
# ----------------------------------


s = "cbacdcbc"

obj = Solution()

print(

    obj.smallestSubsequence(

        s

    )

)

# Output:
# acdb