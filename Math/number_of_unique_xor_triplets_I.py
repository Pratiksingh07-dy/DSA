class Solution:

    def uniqueXorTriplets(
        self,
        nums
    ):

        n = len(nums)

        if n <= 2:

            return n

        bits = n.bit_length()

        return 1 << bits


# ----------------------------------
# Pattern Used:
#
# Math
# +
# XOR
#
#
# My Thinking:
#
# nums is always a
# permutation of:
#
# [1, 2, ..., n]
#
# So the actual order
# does not matter.
#
# For n = 1:
# answer = 1
#
# For n = 2:
# answer = 2
#
# For n >= 3:
# all XOR values from
# 0 to 2^bits - 1
# can be formed.
#
# Therefore:
#
# answer = 2^bits
#
#
# Time Complexity:
#
# O(1)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


nums = [

    3,

    1,

    2

]


obj = Solution()


result = obj.uniqueXorTriplets(

    nums

)


print(result)


# Output:
# 4