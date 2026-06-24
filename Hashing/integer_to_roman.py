class Solution:

    def intToRoman(self, num):

        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        answer = []

        for i in range(len(values)):

            while num >= values[i]:

                answer.append(symbols[i])

                num -= values[i]

        return "".join(answer)


# Test

num = 1994

obj = Solution()

print(
    obj.intToRoman(num)
)

# Output:
# MCMXCIV


# -----------------------------
# Pattern Used:
# Hash Map + Greedy
#
# Why:
# Always use the largest
# Roman value possible.
#
# My thinking:
# 1. Store Roman values
#    from largest to smallest.
# 2. Take largest possible.
# 3. Subtract from number.
# 4. Repeat until number = 0.
#
# Example:
#
# num = 1994
#
# 1000 -> M
# 900  -> CM
# 90   -> XC
# 4    -> IV
#
# Answer:
# MCMXCIV
#
# Time Complexity: O(1)
#
# Space Complexity: O(1)
# -----------------------------