class Solution:

    def missingIntegers(
        self,
        nums
    ):

        # Store all numbers
        # for O(1) lookup

        present = set(

            nums

        )


        smallest = min(

            nums

        )

        largest = max(

            nums

        )


        answer = []


        # Check every number
        # in the range

        for num in range(

            smallest,

            largest + 1

        ):

            if num not in present:

                answer.append(

                    num

                )


        return answer


# ----------------------------------
# Pattern Used:
#
# Arrays
#
# +
#
# Hash Set
#
#
# My Thinking:
#
# 1. Find the
#    smallest number.
#
# 2. Find the
#    largest number.
#
# 3. Store all
#    numbers in a set.
#
# 4. Traverse every
#    integer in the
#    range.
#
# 5. If it is not in
#    the set, it is
#    missing.
#
#
# Time Complexity:
#
# O(n + range)
#
#
# Space Complexity:
#
# O(n)
# ----------------------------------


nums = [

    1,

    4,

    2,

    5

]


obj = Solution()

result = obj.missingIntegers(

    nums

)

print(result)

# Output:
# [3]