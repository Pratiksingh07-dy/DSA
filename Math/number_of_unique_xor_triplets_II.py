class Solution:

    def uniqueXorTriplets(
        self,
        nums
    ):

        # Store all possible
        # XOR values of 2 numbers

        pairXor = set()

        for a in nums:

            for b in nums:

                pairXor.add(

                    a ^ b

                )


        # Store all possible
        # XOR values of 3 numbers

        result = set()

        for value in pairXor:

            for num in nums:

                result.add(

                    value ^ num

                )


        return len(result)


# ----------------------------------
# Pattern Used:
#
# Math
# +
# XOR
# +
# Hashing (Set)
#
#
# My Thinking:
#
# Instead of trying all:
#
# i, j, k
#
# which would be O(n³),
#
# first calculate all
# unique XOR values of:
#
# nums[i] XOR nums[j]
#
# Then XOR each of those
# values with every number.
#
#
# Time Complexity:
#
# O(n² + X * n)
#
# Here X is bounded by
# the number of possible
# XOR values.
#
# Since nums[i] <= 1500,
# XOR values are below 2048.
#
# So effectively:
#
# O(n² + 2048n)
#
#
# Space Complexity:
#
# O(2048)
# ----------------------------------


nums = [

    1,

    3

]


obj = Solution()


result = obj.uniqueXorTriplets(

    nums

)


print(result)


# Output:
# 2