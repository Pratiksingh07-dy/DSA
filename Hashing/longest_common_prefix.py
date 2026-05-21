class Solution:
    def longestCommonPrefix(self, arr1, arr2):

        prefixes = set()

        for num in arr1:

            num = str(num) # we took str because we cant convert number into text 

            for i in range(1, len(num)+1):
                prefixes.add(num[:i])

        longest = 0

        for num in arr2:

            num = str(num)

            for i in range(1, len(num)+1):

                prefix = num[:i]

                if prefix in prefixes:
                    longest = max(
                        longest,
                        len(prefix)
                    )

        return longest


# Test Code
arr1=[1,10,100,1000]
arr2=[1000]

obj=Solution()

answer=obj.longestCommonPrefix(arr1,arr2)

print("Longest Prefix Length:",answer)



# Pattern Used: Hashing
#
# My thinking:
# 1. Generate all prefixes from arr1
# 2. Store prefixes in set
# 3. Generate prefixes from arr2
# 4. Check if prefix exists
# 5. Store maximum prefix length
#
# 3043. Find the Length of the Longest Common Prefix