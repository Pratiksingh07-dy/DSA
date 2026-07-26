class Solution:

    def maximumProduct(
        self,
        nums
    ):

        nums.sort()


        return max(

            nums[-1]

            *

            nums[-2]

            *

            nums[-3],


            nums[0]

            *

            nums[1]

            *

            nums[-1]

        )


# ----------------------------------
# Pattern Used:
#
# Arrays
#
# +
#
# Sorting
#
#
# My Thinking:
#
# After sorting,
# only two cases
# can give the
# maximum product.
#
# Case 1:
#
# Three largest
# numbers.
#
# Case 2:
#
# Two smallest
# (most negative)
# numbers and the
# largest positive
# number.
#
# Return the
# maximum of both.
#
#
# Time Complexity:
#
# O(n log n)
#
#
# Space Complexity:
#
# O(1)
# ----------------------------------


nums = [

    -10,

    -10,

    5,

    2

]


obj = Solution()


result = obj.maximumProduct(

    nums

)


print(result)

# Output:
# 500