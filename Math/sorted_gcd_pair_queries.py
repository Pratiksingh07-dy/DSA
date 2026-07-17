from bisect import bisect_right


class Solution:

    def gcdValues(
        self,
        nums,
        queries
    ):

        maxNum = max(nums)

        # Count frequency
        # of every number

        freq = [

            0

        ] * (

            maxNum + 1

        )

        for num in nums:

            freq[num] += 1


        # gcdCount[g]
        #
        # Number of pairs
        # whose exact GCD
        # is g

        gcdCount = [

            0

        ] * (

            maxNum + 1

        )


        for g in range(

            maxNum,

            0,

            -1

        ):

            count = 0

            # Count numbers
            # divisible by g

            for multiple in range(

                g,

                maxNum + 1,

                g

            ):

                count += freq[multiple]


            # Total pairs where
            # both numbers are
            # divisible by g

            gcdCount[g] = (

                count

                *

                (count - 1)

                //

                2

            )


            # Remove pairs whose
            # exact GCD is a
            # multiple of g

            for multiple in range(

                g * 2,

                maxNum + 1,

                g

            ):

                gcdCount[g] -= (

                    gcdCount[multiple]

                )


        # Prefix count

        prefix = [

            0

        ] * (

            maxNum + 1

        )

        for g in range(

            1,

            maxNum + 1

        ):

            prefix[g] = (

                prefix[g - 1]

                +

                gcdCount[g]

            )


        # Answer queries
        # using binary search

        answer = []

        for query in queries:

            gcdValue = bisect_right(

                prefix,

                query

            )

            answer.append(

                gcdValue

            )

        return answer


# ----------------------------------
# Pattern Used:
#
# Math
#
# +
#
# Divisor Counting
#
# +
#
# Binary Search
#
#
# Time Complexity:
#
# Approximately:
#
# O(M log M + Q log M)
#
# M = max(nums)
#
#
# Space Complexity:
#
# O(M)
# ----------------------------------


nums = [

    2,

    3,

    4

]

queries = [

    0,

    2,

    2

]


obj = Solution()

print(

    obj.gcdValues(

        nums,

        queries

    )

)


# Output:
#
# [1, 2, 2]