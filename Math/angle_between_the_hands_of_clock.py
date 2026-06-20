class Solution:

    def angleClock(self, hour, minutes):

        minute_angle = minutes * 6

        hour_angle = (
            (hour % 12) * 30
            + minutes * 0.5
        )

        angle = abs(
            hour_angle - minute_angle
        )

        return min(
            angle,
            360 - angle
        )


# Test Code

hour = 3
minutes = 30

obj = Solution()

answer = obj.angleClock(
    hour,
    minutes
)

print(answer)


# -----------------------------
# Pattern Used:
# Math
#
# Why:
# Need angle between
# hour hand and minute hand.
#
# My thinking:
# 1. Find minute hand angle
# 2. Find hour hand angle
# 3. Calculate difference
# 4. Return smaller angle
#
# Formula:
#
# minute_angle =
# minutes * 6
#
# hour_angle =
# (hour % 12) * 30
# + minutes * 0.5
#
# Example:
#
# 3:30
#
# Minute hand:
# 30 * 6 = 180
#
# Hour hand:
# 3 * 30 + 30 * 0.5
# = 105
#
# Difference:
# 75
#
# Time Complexity: O(1)
# Space Complexity: O(1)
# -----------------------------