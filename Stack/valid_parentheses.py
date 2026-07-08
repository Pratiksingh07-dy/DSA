class Solution:

    def isValid(
        self,
        s
    ):

        stack = []

        mapping = {

            ')': '(',

            ']': '[',

            '}': '{'

        }

        for ch in s:

            if ch in mapping:

                if (
                    not stack
                    or
                    stack.pop() != mapping[ch]
                ):

                    return False

            else:

                stack.append(ch)

        return (
            len(stack) == 0
        )


# -----------------------------
# Pattern Used:
#
# Stack
#
#
# Why:
#
# The last opening
# bracket must be
# matched first.
#
# Stack follows
# LIFO
# (Last In First Out),
# making it perfect.
#
#
# My Thinking:
#
# 1. Push every
#    opening bracket.
#
# 2. When a closing
#    bracket comes,
#    check whether
#    the top of stack
#    matches it.
#
# 3. If not,
#    return False.
#
# 4. At the end,
#    stack must
#    be empty.
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
# -----------------------------


s = "([])"

obj = Solution()

print(
    obj.isValid(
        s
    )
)

# Output:
# True