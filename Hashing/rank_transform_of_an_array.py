class Solution:

    def arrayRankTransform(
        self,
        arr
    ):

        sortedUnique = sorted(

            set(arr)

        )

        rank = {}

        currentRank = 1

        for num in sortedUnique:

            rank[num] = currentRank

            currentRank += 1

        answer = []

        for num in arr:

            answer.append(

                rank[num]

            )

        return answer


# ----------------------------------
# Pattern Used:
#
# Sorting
#
# +
#
# Hash Map
#
#
# Why:
#
# Sort the unique
# elements.
#
# Assign increasing
# ranks.
#
# Use a hash map to
# replace every element
# with its rank.
#
#
# My Thinking:
#
# 1. Remove duplicates.
#
# 2. Sort remaining
#    values.
#
# 3. Assign ranks
#    starting from 1.
#
# 4. Replace every
#    element using
#    the hash map.
#
#
# Time Complexity:
#
# O(n log n)
#
#
# Space Complexity:
#
# O(n)
# ----------------------------------


arr = [

    40,

    10,

    20,

    30

]

obj = Solution()

print(

    obj.arrayRankTransform(

        arr

    )

)

# Output:
# [4, 1, 2, 3]