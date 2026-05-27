class Solution:
    def plusOne(self, digits):

        n = len(digits)

        for i in range(n-1,-1,-1):

            if digits[i] < 9:

                digits[i] += 1

                return digits

            digits[i] = 0

        return [1] + digits


# 66. Plus one sum

# Test Code
digits=[1,2,3]

obj=Solution()

answer=obj.plusOne(digits)

print(answer)



# Pattern Used: Array Traversal
#
# Why:
# Need to add one while handling carry.
#
# My thinking:
# 1. Start from last digit
# 2. If digit < 9, add 1 and stop
# 3. If digit is 9, make it 0
# 4. Continue carry to left side
# 5. If all digits become 0,
#    add 1 at front
#
# Time Complexity: O(n)
