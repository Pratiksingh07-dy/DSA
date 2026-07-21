class Solution:

    def reverse(
        self,
        x
    ):

        INT_MIN = -2 ** 31

        INT_MAX = 2 ** 31 - 1

        # Store the sign

        if x < 0:

            sign = -1

        else:

            sign = 1


        # Make number positive

        x = abs(x)


        reversedNum = 0


        # Reverse the digits

        while x > 0:

            # Get last digit

            digit = x % 10


            # Remove last digit

            x //= 10


            # Add digit to
            # reversed number

            reversedNum = (

                reversedNum * 10

                +

                digit

            )


        # Add original sign

        reversedNum *= sign


        # Check 32-bit range

        if (

            reversedNum < INT_MIN

            or

            reversedNum > INT_MAX

        ):

            return 0


        return reversedNum


# ----------------------------------
# Pattern Used:
#
# Math
#
#
# My Thinking:
#
# 1. Save the sign.
#
# 2. Make x positive.
#
# 3. Extract the last
#    digit using % 10.
#
# 4. Remove the last
#    digit using // 10.
#
# 5. Build the reversed
#    number.
#
# 6. Restore the sign.
#
# 7. Check 32-bit range.
#
#
# Time Complexity:
#
# O(log x)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


x = -123

obj = Solution()

result = obj.reverse(

    x

)

print(result)


# Output:
# -321