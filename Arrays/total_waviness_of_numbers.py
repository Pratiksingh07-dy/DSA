#3751. Total Waviness of Numbers in Range I

class Solution:
    def totalWaviness(self, num1, num2):

        total = 0

        for num in range(num1, num2 + 1):

            digits = str(num)

            waviness = 0

            for i in range(1, len(digits) - 1):

                left = int(digits[i - 1])
                mid = int(digits[i])
                right = int(digits[i + 1])

                if mid > left and mid > right:
                    waviness += 1

                elif mid < left and mid < right:
                    waviness += 1

            total += waviness

        return total


# Test Code

num1 = 120
num2 = 130

obj = Solution()

answer = obj.totalWaviness(
    num1,
    num2
)

print(answer)



# Pattern Used: Digit Processing
#
# Why:
# Need to check each digit and
# determine whether it is a
# peak or valley.
#
# My thinking:
# 1. Traverse all numbers
# 2. Convert number to string
# 3. Check every middle digit
# 4. Count peaks and valleys
# 5. Add waviness to answer
#
# Time Complexity:
# O((num2-num1+1) * digits)
#
