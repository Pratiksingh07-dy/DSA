from collections import Counter


class Solution:

    def maxNumberOfBalloons(self, text):

        count = Counter(text)

        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )


# Test

text = "loonbalxballpoon"

obj = Solution()

print(
    obj.maxNumberOfBalloons(text)
)

# Output:
# 2


# -----------------------------
# Pattern Used:
# Hashing / Frequency Count
#
# Why:
# Need to count how many
# times each character appears.
#
# My thinking:
# 1. Count frequency of all letters.
# 2. Word needed = "balloon"
# 3. b,a,n needed once.
# 4. l,o needed twice.
# 5. Find limiting character.
#
# Example:
#
# text =
# "loonbalxballpoon"
#
# Counts:
# b = 2
# a = 2
# l = 4
# o = 4
# n = 2
#
# Possible balloons:
#
# b -> 2
# a -> 2
# l -> 4//2 = 2
# o -> 4//2 = 2
# n -> 2
#
# Answer = min(...)
# = 2
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------