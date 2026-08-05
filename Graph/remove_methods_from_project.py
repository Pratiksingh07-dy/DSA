class Solution:

    def remainingMethods(
        self,
        n,
        k,
        invocations
    ):

        # Build graph

        graph = [

            []

            for _ in range(n)

        ]

        for u, v in invocations:

            graph[u].append(

                v

            )


        # Mark suspicious
        # methods

        suspicious = [

            False

        ] * n


        def dfs(

            node

        ):

            suspicious[node] = True

            for nei in graph[node]:

                if not suspicious[nei]:

                    dfs(

                        nei

                    )


        dfs(k)


        # If a non-suspicious
        # method calls a
        # suspicious one,
        # removal is impossible.

        for u, v in invocations:

            if (

                not suspicious[u]

                and

                suspicious[v]

            ):

                return list(

                    range(n)

                )


        answer = []

        for i in range(

            n

        ):

            if not suspicious[i]:

                answer.append(

                    i

                )

        return answer


# ----------------------------------
# Pattern Used:
#
# Graph
#
# +
#
# DFS
#
#
# My Thinking:
#
# 1. Build graph.
#
# 2. DFS from k.
#
# 3. Every reachable
#    method becomes
#    suspicious.
#
# 4. Check whether
#    any safe method
#    calls a suspicious
#    method.
#
# 5. If yes,
#    removal is
#    impossible.
#
# 6. Otherwise return
#    all non-suspicious
#    methods.
#
#
# Time Complexity:
#
# O(n + m)
#
#
# Space Complexity:
#
# O(n + m)
# ----------------------------------


n = 5

k = 0

invocations = [

    [1, 2],

    [0, 2],

    [0, 1],

    [3, 4]

]


obj = Solution()

print(

    obj.remainingMethods(

        n,

        k,

        invocations

    )

)

# Output:
# [3, 4]