class Solution:

    def stringSequence(self, words, weights):

        answer = []

        for word in words:

            total = 0

            for ch in word:

                total += weights[
                    ord(ch) - ord('a')
                ]

            remainder = total % 26

            answer.append(
                chr(
                    ord('z') - remainder
                )
            )

        return "".join(answer)


# Test Code

words = ["abcd", "def", "xyz"]

weights = [
    5,3,12,14,1,2,3,2,10,6,6,9,7,
    8,7,10,8,9,6,9,9,8,3,7,7,2
]

obj = Solution()

result = obj.stringSequence(
    words,
    weights
)

print("Answer:", result)


# -----------------------------
# Pattern Used:
# Array Traversal + Strings
#
# Why:
# Need to calculate weight
# of each word.
#
# My thinking:
# 1. Traverse every word
# 2. Calculate word weight
# 3. Take modulo 26
# 4. Convert result into
#    reverse alphabet letter
# 5. Join all letters
#
# Example:
#
# abcd
#
# weight:
# 5+3+12+14
# = 34
#
# 34 % 26 = 8
#
# 8 -> r
#
# Time Complexity:
# O(total characters)
#
# Space Complexity:
# O(words.length)
# -----------------------------