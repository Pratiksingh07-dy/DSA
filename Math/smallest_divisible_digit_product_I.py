class Solution:

    def smallestNumber(
        self,
        n,
        t
    ):

        while True:

            product = 1


            # Find product
            # of digits

            for digit in str(

                n

            ):

                product *= int(

                    digit

                )


            # Check divisibility

            if (

                product % t

                == 0

            ):

                return n


            n += 1


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
# Start from n.
#
# Find the product
# of its digits.
#
# If product is
# divisible by t,
# return n.
#
# Otherwise,
# check the next
# number.
#
#
# Time Complexity:
#
# O(k × d)
#
# k = numbers checked
#
# d = number of digits
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


n = 15

t = 3


obj = Solution()

result = obj.smallestNumber(

    n,

    t

)

print(result)

# Output:
# 16