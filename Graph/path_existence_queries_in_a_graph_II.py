class Solution:

    def pathExistenceQueries(
        self,
        n,
        nums,
        maxDiff,
        queries
    ):

        pairs = sorted(

            (
                nums[i],
                i
            )

            for i in range(n)

        )

        LOG = 20

        jump = [

            [0] * LOG

            for _ in range(n)

        ]

        right = n - 1

        for left in range(

            n - 1,
            -1,
            -1

        ):

            while (

                pairs[right][0]
                -
                pairs[left][0]

                >

                maxDiff

            ):

                right -= 1

            currentNode = pairs[left][1]

            farthestNode = pairs[right][1]

            jump[currentNode][0] = farthestNode

            for power in range(

                1,
                LOG

            ):

                jump[currentNode][power] = (

                    jump[

                        jump[currentNode][power - 1]

                    ][power - 1]

                )

        answer = []

        for u, v in queries:

            if nums[u] > nums[v]:

                u, v = v, u

            if u == v:

                answer.append(0)

                continue

            if nums[u] == nums[v]:

                answer.append(1)

                continue

            distance = 0

            for power in range(

                LOG - 1,
                -1,
                -1

            ):

                if (

                    nums[

                        jump[u][power]

                    ]

                    <

                    nums[v]

                ):

                    distance |= (

                        1 << power

                    )

                    u = jump[u][power]

            if (

                nums[

                    jump[u][0]

                ]

                <

                nums[v]

            ):

                answer.append(-1)

            else:

                answer.append(

                    distance + 1

                )

        return answer


# ----------------------------------
# Pattern Used:
#
# Graph
#
# +
#
# Sorting
#
# +
#
# Binary Lifting
#
# (Sparse Table)
#
#
# Why:
#
# Sort the nodes by value.
#
# For every node,
# precompute the
# farthest node
# reachable in one move.
#
# Binary Lifting lets
# us jump
# 2^k steps at once,
# reducing query time.
#
#
# My Thinking:
#
# 1. Sort nodes
#    according to nums.
#
# 2. Build the first
#    jump table.
#
# 3. Build higher
#    jumps using
#    Sparse Table.
#
# 4. For each query,
#    greedily take the
#    biggest jump that
#    still keeps us
#    before the target.
#
# 5. Count jumps.
#
#
# Time Complexity:
#
# Preprocessing:
#
# O(n log n)
#
#
# Each Query:
#
# O(log n)
#
#
# Overall:
#
# O((n + q) log n)
#
#
# Space Complexity:
#
# O(n log n)
# ----------------------------------


n = 5

nums = [

    5,
    3,
    1,
    9,
    10

]

maxDiff = 2

queries = [

    [0,1],

    [0,2],

    [2,3],

    [4,3]

]

obj = Solution()

print(

    obj.pathExistenceQueries(

        n,

        nums,

        maxDiff,

        queries

    )

)

# Output:
# [1, 2, -1, 1]