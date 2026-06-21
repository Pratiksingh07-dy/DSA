class Solution:

    def romanToInt(self, s):

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        answer = 0

        for i in range(len(s)):

            if (
                i < len(s) - 1
                and roman[s[i]] < roman[s[i + 1]]
            ):

                answer -= roman[s[i]]

            else:

                answer += roman[s[i]]

        return answer


# Test

s = "MCMXCIV"

obj = Solution()

print(
    obj.romanToInt(s)
)

# Output:
# 1994


# -----------------------------
# Pattern Used:
# Hash Map
#
# Why:
# Need quick lookup of Roman
# symbol values.
#
# My thinking:
# 1. Store Roman values in hash map.
# 2. Traverse string.
# 3. If current value is smaller
#    than next value, subtract it.
# 4. Otherwise add it.
# 5. Return final answer.
#
# Example:
#
# IV
#
# I < V
#
# = -1 + 5
#
# = 4
#
# Example:
#
# MCMXCIV
#
# M = 1000
# CM = 900
# XC = 90
# IV = 4
#
# Total = 1994
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------