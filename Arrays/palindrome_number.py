class Solution:
    def isPalindrome(self, x):

        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:

             = x % 10

            reversed_num = reversed_num * 10 + 

            x //= 10

        return original == reversed_num


# Test Code
x = 1213121

obj = Solution()

answer = obj.isPalindrome(x)

print(answer)



# Pattern Used: Number Reversal
#
# My thinking:
# 1. Store original number
# 2. Reverse the number
# 3. Compare original and reversed
# 4. If same -> palindrome
#
# Time Complexity: O(log n)
