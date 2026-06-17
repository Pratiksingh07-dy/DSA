class Solution:

    def longestPalindrome(self, s):

        answer = ""

        def expand(left, right):

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):

                left -= 1
                right += 1

            return s[left + 1:right]

        for i in range(len(s)):

            odd = expand(i, i)

            if len(odd) > len(answer):

                answer = odd

            even = expand(i, i + 1)

            if len(even) > len(answer):

                answer = even

        return answer


# Test Code

s = "babad"

obj = Solution()

result = obj.longestPalindrome(s)

print("Answer:", result)


# -----------------------------
# Pattern Used:
# Expand Around Center
#
# Why:
# Every palindrome has a center.
#
# My thinking:
# 1. Take every index as center
# 2. Expand left and right
# 3. Check odd palindrome
# 4. Check even palindrome
# 5. Store longest palindrome
#
# Example:
#
# babad
#
# Center = a
#
# b a b
#
# Expands to "bab"
#
# Answer = "bab"
#
# Time Complexity:
# O(n²)
#
# Space Complexity:
# O(1)
# -----------------------------