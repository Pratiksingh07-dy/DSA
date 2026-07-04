from collections import defaultdict


class Solution:

    def minScore(
        self,
        n,
        roads
    ):

        graph = defaultdict(list)

        for u, v, weight in roads:

            graph[u].append(
                (
                    v,
                    weight
                )
            )

            graph[v].append(
                (
                    u,
                    weight
                )
            )

        visited = set()

        answer = float("inf")

        def dfs(node):

            nonlocal answer

            visited.add(node)

            for nxt, weight in graph[node]:

                answer = min(
                    answer,
                    weight
                )

                if nxt not in visited:

                    dfs(nxt)

        dfs(1)

        return answer


# -----------------------------
# Pattern Used:
#
# Graph
#
# ↓
#
# DFS
#
# ↓
#
# Connected Component
#
#
# Why:
#
# We can visit roads
# multiple times.
#
# So every road inside
# the connected component
# of city 1 can be used.
#
# Therefore answer is
# simply the minimum edge
# weight in that component.
#
#
# My Thinking:
#
# Step 1
#
# Build graph.
#
# Step 2
#
# DFS from city 1.
#
# Step 3
#
# While traversing,
# keep updating the
# smallest edge seen.
#
# Step 4
#
# Return it.
#
#
# Time Complexity:
#
# O(V + E)
#
#
# Space Complexity:
#
# O(V + E)
# -----------------------------


# Test

n = 4

roads = [
    [1,2,9],
    [2,3,6],
    [2,4,5],
    [1,4,7]
]

obj = Solution()

print(
    obj.minScore(
        n,
        roads
    )
)

# Output:
# 5