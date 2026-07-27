class Solution:

    def maxProduct(
        self,
        nums
    ):

        nums.sort()


        return (

            nums[-1]

            - 1

        ) * (

            nums[-2]

            - 1

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
# 1. Sort the array.
#
# 2. The two largest
#    numbers will give
#    the maximum value.
#
# 3. Apply:
#
#    (a - 1) * (b - 1)
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

    3,

    4,

    5,

    2

]


obj = Solution()


result = obj.maxProduct(

    nums

)


print(result)

# Output:
# 12