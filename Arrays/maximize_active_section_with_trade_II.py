from bisect import bisect_left, bisect_right


class Solution:

    def maxActiveSectionsAfterTrade(
        self,
        s,
        queries
    ):

        n = len(s)

        total_ones = s.count('1')


        # Store all zero groups:
        # (start, end, length)

        groups = []

        i = 0

        while i < n:

            if s[i] == '0':

                start = i

                while (

                    i < n

                    and

                    s[i] == '0'

                ):

                    i += 1

                groups.append(

                    (

                        start,

                        i - 1,

                        i - start

                    )

                )

            else:

                i += 1


        m = len(groups)


        # If there are fewer
        # than 2 zero groups,
        # no trade is possible

        if m < 2:

            return [

                total_ones

                for _ in queries

            ]


        # Calculate gain for
        # consecutive zero groups

        pair = []

        for i in range(m - 1):

            pair.append(

                groups[i][2]

                +

                groups[i + 1][2]

            )


        # Build Segment Tree

        size = 1

        while size < len(pair):

            size *= 2


        tree = [

            0

        ] * (

            2 * size

        )


        for i, value in enumerate(pair):

            tree[size + i] = value


        for i in range(

            size - 1,

            0,

            -1

        ):

            tree[i] = max(

                tree[i * 2],

                tree[i * 2 + 1]

            )


        # Segment Tree
        # Range Maximum Query

        def range_max(

            left,

            right

        ):

            if left > right:

                return 0


            left += size

            right += size

            result = 0


            while left <= right:

                if left % 2 == 1:

                    result = max(

                        result,

                        tree[left]

                    )

                    left += 1


                if right % 2 == 0:

                    result = max(

                        result,

                        tree[right]

                    )

                    right -= 1


                left //= 2

                right //= 2


            return result


        starts = [

            group[0]

            for group in groups

        ]


        ends = [

            group[1]

            for group in groups

        ]


        answer = []


        # Process each query

        for l, r in queries:

            first = bisect_left(

                ends,

                l

            )


            last = bisect_right(

                starts,

                r

            ) - 1


            # We need at least
            # two zero groups

            if first >= last:

                answer.append(

                    total_ones

                )

                continue


            best = 0


            # Check first pair

            first_len = (

                ends[first]

                -

                max(

                    starts[first],

                    l

                )

                +

                1

            )


            second_len = (

                min(

                    ends[first + 1],

                    r

                )

                -

                starts[first + 1]

                +

                1

            )


            best = max(

                best,

                first_len

                +

                second_len

            )


            # Check last pair

            previous_len = (

                ends[last - 1]

                -

                max(

                    starts[last - 1],

                    l

                )

                +

                1

            )


            last_len = (

                min(

                    ends[last],

                    r

                )

                -

                starts[last]

                +

                1

            )


            best = max(

                best,

                previous_len

                +

                last_len

            )


            # Check fully contained
            # zero-group pairs

            if (

                first + 1

                <=

                last - 2

            ):

                best = max(

                    best,

                    range_max(

                        first + 1,

                        last - 2

                    )

                )


            answer.append(

                total_ones

                +

                best

            )


        return answer


# ----------------------------------
# Pattern Used:
#
# Arrays
#
# +
#
# Binary Search
#
# +
#
# Segment Tree
#
#
# My Thinking:
#
# 1. Count total 1s
#    in original string.
#
# 2. Find all continuous
#    zero groups.
#
# 3. A valid trade joins
#    two zero groups that
#    have a 1-group
#    between them.
#
# 4. The gain is:
#
#    left zero length
#    +
#    right zero length
#
# 5. For every query,
#    find zero groups
#    inside its range.
#
# 6. Use Segment Tree
#    to quickly find
#    maximum gain.
#
#
# Time Complexity:
#
# O(n + q log n)
#
#
# Space Complexity:
#
# O(n)
# ----------------------------------


s = "0100"

queries = [

    [0, 3],

    [0, 2],

    [1, 3],

    [2, 3]

]


obj = Solution()


result = (

    obj.maxActiveSectionsAfterTrade(

        s,

        queries

    )

)


print(result)


# Output:
#
# [4, 3, 1, 1]