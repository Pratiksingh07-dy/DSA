class Solution:

    def largestAltitude(self, gain):

        altitude = 0

        highest = 0

        for g in gain:

            altitude += g

            highest = max(
                highest,
                altitude
            )

        return highest


# Test Code

gain = [-5,1,5,0,-7]

obj = Solution()

answer = obj.largestAltitude(gain)

print(answer)


# -----------------------------
# Pattern Used:
# Prefix Sum
#
# Why:
# Current altitude depends
# on previous altitude.
#
# My thinking:
# 1. Start altitude = 0
# 2. Add each gain
# 3. Track highest altitude
# 4. Return maximum
#
# Example:
#
# gain =
# [-5,1,5,0,-7]
#
# Altitudes:
# 0
# -5
# -4
# 1
# 1
# -6
#
# Highest = 1
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------