from collections import deque


class Solution:

    def assignEdgeWeights(self, edges, queries):

        MOD = 10**9 + 7

        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:

            graph[u].append(v)
            graph[v].append(u)

        LOG = 1

        while (1 << LOG) <= n:
            LOG += 1

        parent = [[0] * (n + 1) for _ in range(LOG)]

        depth = [0] * (n + 1)

        visited = [False] * (n + 1)

        queue = deque([1])

        visited[1] = True

        while queue:

            node = queue.popleft()

            for neighbor in graph[node]:

                if not visited[neighbor]:

                    visited[neighbor] = True

                    depth[neighbor] = depth[node] + 1

                    parent[0][neighbor] = node

                    queue.append(neighbor)

        for j in range(1, LOG):

            for i in range(1, n + 1):

                parent[j][i] = parent[j - 1][
                    parent[j - 1][i]
                ]

        def lca(u, v):

            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):

                if diff & (1 << j):

                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):

                if parent[j][u] != parent[j][v]:

                    u = parent[j][u]

                    v = parent[j][v]

            return parent[0][u]

        answer = []

        for u, v in queries:

            ancestor = lca(u, v)

            distance = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )

            if distance == 0:

                answer.append(0)

            else:

                answer.append(
                    pow(
                        2,
                        distance - 1,
                        MOD
                    )
                )

        return answer


# Test Code

edges = [
    [1, 2],
    [1, 3],
    [3, 4],
    [3, 5]
]

queries = [
    [1, 4],
    [3, 4],
    [2, 5]
]

obj = Solution()

result = obj.assignEdgeWeights(
    edges,
    queries
)

print("Answer:", result)


# -----------------------------
# Pattern Used:
# Tree + LCA (Binary Lifting)
#
# Why:
# Need distance between
# any two nodes quickly
# for up to 100000 queries.
#
# My thinking:
# 1. Build adjacency list
# 2. BFS from root node 1
# 3. Store depth of every node
# 4. Build parent table
#    for Binary Lifting
# 5. Find LCA(u,v)
# 6. Distance =
#    depth[u] + depth[v]
#    - 2*depth[lca]
# 7. Path has d edges
# 8. Total assignments = 2^d
# 9. Half give odd sum
# 10. Answer = 2^(d-1)
#
# Example:
#
# Query = [2,5]
#
# Path:
# 2 -> 1 -> 3 -> 5
#
# Distance = 3
#
# Total assignments:
# 2^3 = 8
#
# Odd assignments:
# 4
#
# Answer:
# 2^(3-1) = 4
#
# Time Complexity:
# O((n+q) log n)
#
# Space Complexity:
# O(n log n)
# -----------------------------