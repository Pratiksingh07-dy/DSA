#3121 Count the number of special character ii
class Solution:
    def numberOfSpecialChars(self, word):

        lastLower = {}
        firstUpper = {}

        for i,ch in enumerate(word):

            if ch.islower():

                lastLower[ch] = i

            else:

                ch = ch.lower()

                if ch not in firstUpper:
                    firstUpper[ch] = i

        count = 0

        for ch in lastLower:

            if (ch in firstUpper and
                lastLower[ch] < firstUpper[ch]):

                count += 1

        return count


# Test Code
word="aaAbcBC"

obj=Solution()

answer=obj.numberOfSpecialChars(word)

print("Special characters:",answer)

#not much different than previous sum, just need to have a condition



# Pattern Used: HashMap + Index Tracking
#
# Why:
# Need to remember positions
# of lowercase and uppercase.
#
# My thinking:
# 1. Store last lowercase index
# 2. Store first uppercase index
# 3. Compare positions
# 4. Count valid letters
#
# Time Complexity: O(n)