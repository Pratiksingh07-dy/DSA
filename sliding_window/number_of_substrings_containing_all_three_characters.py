class Solution:

    def numberOfSubstrings(self, s):

        count = {
            'a': 0,
            'b': 0,
            'c': 0
        }

        left = 0

        answer = 0

        for right in range(len(s)):

            count[s[right]] += 1

            while (
                count['a'] > 0 and
                count['b'] > 0 and
                count['c'] > 0
            ):

                answer += len(s) - right

                count[s[left]] -= 1

                left += 1

        return answer


# -----------------------------
# Pattern Used:
# Sliding Window + Two Pointers
#
# Why:
# Need to count all valid
# substrings efficiently.
#
# My thinking:
# 1. Expand window.
# 2. Keep counts of a,b,c.
# 3. When all exist,
#    every extension to
#    the right is also valid.
# 4. Count them.
# 5. Shrink window.
#
# Example:
#
# s = "abcabc"
#
# First valid:
#
# abc
#
# Remaining endings:
#
# abc
# abca
# abcab
# abcabc
#
# Count = 4
#
# Time Complexity:
# O(n)
#
# Reason:
# Every character enters
# and leaves the window once.
#
# Space Complexity:
# O(1)
# -----------------------------


# Test

s = "abcabc"

obj = Solution()

print(
    obj.numberOfSubstrings(
        s
    )
)

# Output:
# 10