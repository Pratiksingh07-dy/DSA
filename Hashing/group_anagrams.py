class Solution:

    def groupAnagrams(
        self,
        strs
    ):

        groups = {}


        # Process every word

        for word in strs:

            # Frequency of
            # each character

            count = [0] * 26


            for ch in word:

                count[

                    ord(ch)
                    -
                    ord('a')

                ] += 1


            # Convert list to tuple
            # so it can be used
            # as a dictionary key

            key = tuple(

                count

            )


            if key not in groups:

                groups[key] = []


            groups[key].append(

                word

            )


        return list(

            groups.values()

        )


# ----------------------------------
# Pattern Used:
#
# Hashing
#
# +
#
# Frequency Count
#
#
# Main Idea:
#
# Anagrams have exactly
# the same character
# frequencies.
#
# "eat"
#
# e = 1
# a = 1
# t = 1
#
# "tea"
#
# e = 1
# a = 1
# t = 1
#
# Therefore they get
# the same key.
#
#
# Time Complexity:
#
# O(n * k)
#
# n = number of strings
# k = average string length
#
#
# Space Complexity:
#
# O(n * k)
# ----------------------------------


strs = [

    "eat",

    "tea",

    "tan",

    "ate",

    "nat",

    "bat"

]


obj = Solution()

result = obj.groupAnagrams(

    strs

)

print(result)

# Example output:
#
# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]