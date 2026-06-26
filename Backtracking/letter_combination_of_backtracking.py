class Solution:

    def letterCombinations(self, digits):

        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        answer = []

        def backtrack(index, current):

            if index == len(digits):

                answer.append(current)

                return

            letters = phone[digits[index]]

            for letter in letters:

                backtrack(
                    index + 1,
                    current + letter
                )

        backtrack(0, "")

        return answer


# Test

digits = "23"

obj = Solution()

print(
    obj.letterCombinations(
        digits
    )
)

# Output:
# ['ad', 'ae', 'af',
#  'bd', 'be', 'bf',
#  'cd', 'ce', 'cf']


# -----------------------------
# Pattern Used:
# Backtracking (DFS)
#
# Why:
# At every digit we have
# multiple choices.
#
# My thinking:
# 1. Pick one letter from
#    current digit.
# 2. Move to next digit.
# 3. Repeat until all
#    digits are used.
# 4. Store the combination.
#
# Example:
#
# digits = "23"
#
# 2 -> abc
# 3 -> def
#
# Combinations:
#
# ad ae af
# bd be bf
# cd ce cf
#
# Time Complexity:
# O(4^n × n) (There are at most 4 choices for each digit, generating up to 4ⁿ combinations, and each combination takes O(n) time to build)
#
# Space Complexity:
# O(n)
# -----------------------------