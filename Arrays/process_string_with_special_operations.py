class Solution:

    def processStr(self, s):

        result = ""

        for ch in s:

            if ch.isalpha():

                result += ch

            elif ch == "*":

                result = result[:-1]

            elif ch == "#":

                result = result + result

            elif ch == "%":

                result = result[::-1]

        return result


# Test Code

s = "a#b%*"

obj = Solution()

answer = obj.processStr(s)

print(answer)


# -----------------------------
# Pattern Used:
# String Simulation
#
# Why:
# Need to process each
# character according to
# given rules.
#
# My thinking:
# 1. Start with empty string
# 2. Read characters one by one
# 3. Apply operation:
#    letter -> append
#    * -> remove last
#    # -> duplicate
#    % -> reverse
# 4. Return final string
#
# Example:
# a#b%*
#
# a  -> "a"
# #  -> "aa"
# b  -> "aab"
# %  -> "baa"
# *  -> "ba"
#
# Answer = "ba"
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------