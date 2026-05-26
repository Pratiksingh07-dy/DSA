# 3120 Count the numbers of special characters 

class Solution:
    def numberOfSpecialChars(self, word):

        lower = set()
        upper = set()

        for ch in word:

            if ch.islower():
                lower.add(ch)

            else:
                upper.add(ch)

        count = 0

        for ch in lower:

            if ch.upper() in upper:
                count += 1

        return count


# Test Code
word = "aaAbcBCdddEd"

obj = Solution()

answer = obj.numberOfSpecialChars(word)

print("Special characters:",answer)


# -----------------------------
# Pattern Used: Hash Set
#
# Why:
# Need fast checking whether
# lowercase and uppercase exist.
#
# My thinking:
# 1. Store lowercase letters
# 2. Store uppercase letters
# 3. Check if lowercase's uppercase
#    version exists
# 4. Count matches
#
# Time Complexity: O(n)
