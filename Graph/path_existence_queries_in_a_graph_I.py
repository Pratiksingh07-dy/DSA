class Solution:

    def pathExistenceQueries(
        self,
        n,
        nums,
        maxDiff,
        queries
    ):

        parent = list(
            range(n)
        )

        def find(x):

            if parent[x] != x:

                parent[x] = find(
                    parent[x]
                )

            return parent[x]

        def union(x, y):

            parentX = find(x)

            parentY = find(y)

            if parentX != parentY:

                parent[parentY] = parentX

        for i in range(
            n - 1
        ):

            if (
                nums[i + 1]
                - nums[i]
                <= maxDiff
            ):

                union(
                    i,
                    i + 1
                )

        answer = []

        for u, v in queries:

            answer.append(

                find(u)
                ==
                find(v)

            )

        return answer


# ---------------------------------
# Pattern Used:
#
# Graph
#
# +
#
# Union Find (DSU)
#
#
# Why:
#
# If two adjacent numbers
# differ by at most maxDiff,
# they belong to the same
# connected component.
#
# Since nums is sorted,
# checking only adjacent
# elements is enough.
#
#
# My Thinking:
#
# 1. Initially every node
#    is its own parent.
#
# 2. Join adjacent nodes
#    whenever difference
#    <= maxDiff.
#
# 3. For every query,
#    check whether both
#    nodes belong to the
#    same component.
#
#
# Time Complexity:
#
# O(n + q)
#
# (Almost O(1) DSU operations)
#
#
# Space Complexity:
#
# O(n)
# ---------------------------------


n = 4

nums = [
    2,
    5,
    6,
    8
]

maxDiff = 2

queries = [

    [0,1],

    [0,2],

    [1,3],

    [2,3]

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
# [False, False, True, True]