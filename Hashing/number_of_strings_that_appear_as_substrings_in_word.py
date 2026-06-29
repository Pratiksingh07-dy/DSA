class Solution:

    def numOfStrings(self, patterns, word):

        count = 0

        for pattern in patterns:

            if pattern in word:

                count += 1

        return count


# -----------------------------
# Pattern Used:
# String Matching
#
# Why:
# Need to check whether
# every pattern exists
# inside the given word.
#
# My thinking:
# 1. Traverse every pattern.
# 2. Check if it is a
#    substring of word.
# 3. If yes, increase count.
# 4. Return count.
#
# Example:
#
# patterns =
# ["a","abc","bc","d"]
#
# word = "abc"
#
# a   ✓
# abc ✓
# bc  ✓
# d   ✗
#
# Answer = 3
#
# Time Complexity:
# O(n × m)
#
# Reason:
# Check every pattern
# against the word.
#
# Space Complexity:
# O(1)
# -----------------------------


# Test

patterns = ["a","abc","bc","d"]
word = "abc"

obj = Solution()

print(
    obj.numOfStrings(
        patterns,
        word
    )
)

# Output:
# 3