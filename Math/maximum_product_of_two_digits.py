class Solution:

    def maxProduct(
        self,
        n
    ):

        digits = []


        # Extract digits

        while n > 0:

            digits.append(

                n % 10

            )

            n //= 10


        answer = 0

        length = len(digits)


        # Check every pair

        for i in range(

            length

        ):

            for j in range(

                i + 1,

                length

            ):

                answer = max(

                    answer,

                    digits[i]

                    *

                    digits[j]

                )


        return answer


# ----------------------------------
# Pattern Used:
#
# Math
#
# +
#
# Brute Force
#
#
# My Thinking:
#
# 1. Extract every digit.
#
# 2. Store them in a list.
#
# 3. Try every pair.
#
# 4. Keep the maximum
#    product.
#
#
# Time Complexity:
#
# O(d²)
#
# d = number of digits
#
# Maximum digits = 10
#
# So practically O(1)
#
#
# Space Complexity:
#
# O(d)
# ----------------------------------


n = 124

obj = Solution()

result = obj.maxProduct(

    n

)

print(result)

# Output:
# 8