class Solution:

    def addBinary(
        self,
        a,
        b
    ):

        i = len(a) - 1

        j = len(b) - 1

        carry = 0

        answer = []

        while (

            i >= 0

            or

            j >= 0

            or

            carry

        ):

            total = carry

            if i >= 0:

                total += int(

                    a[i]

                )

                i -= 1

            if j >= 0:

                total += int(

                    b[j]

                )

                j -= 1

            answer.append(

                str(

                    total % 2

                )

            )

            carry = (

                total // 2

            )

        return "".join(

            answer[::-1]

        )


# ----------------------------------
# Pattern Used:
#
# Math
#
# +
#
# Simulation
#
#
# Why:
#
# Simulate binary
# addition exactly
# like we do
# decimal addition.
#
#
# My Thinking:
#
# 1. Start from the
#    last digit.
#
# 2. Add both bits
#    and carry.
#
# 3. Store
#    total % 2.
#
# 4. Update carry.
#
# 5. Reverse answer.
#
#
# Time Complexity:
#
# O(max(n,m))
#
#
# Space Complexity:
#
# O(max(n,m))
# ----------------------------------


a = "1010"

b = "1011"

obj = Solution()

print(

    obj.addBinary(

        a,

        b

    )

)

# Output:
# 10101