class Solution:

    def missingInteger(
        self,
        nums
    ):

        # Start with the first
        # element of the prefix

        total = nums[0]


        # Find the longest
        # sequential prefix

        for i in range(

            1,

            len(nums)

        ):

            if nums[i] == nums[i - 1] + 1:

                total += nums[i]

            else:

                break


        # Store all numbers
        # for quick lookup

        present = set(nums)


        # Find the smallest
        # missing number
        # >= prefix sum

        while total in present:

            total += 1


        return total


# ----------------------------------
# Pattern Used:
#
# Arrays
#
# +
#
# Hashing
#
#
# Main Idea:
#
# 1. Find the longest
#    sequential prefix.
#
# 2. Calculate its sum.
#
# 3. Put all nums into
#    a set.
#
# 4. Starting from the
#    sum, keep increasing
#    until we find a
#    number not present.
#
#
# Time Complexity:
#
# O(n)
#
#
# Space Complexity:
#
# O(n)
# ----------------------------------


nums = [

    1,

    2,

    3,

    2,

    5

]


obj = Solution()

result = obj.missingInteger(

    nums

)

print(result)

# Output:
# 6