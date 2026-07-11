class Solution:

    def countCompleteComponents(
        self,
        n,
        edges
    ):

        graph = [

            []

            for _ in range(n)

        ]

        for u, v in edges:

            graph[u].append(v)

            graph[v].append(u)

        visited = [

            False

        ] * n

        def dfs(node):

            visited[node] = True

            component.append(node)

            for neighbor in graph[node]:

                if not visited[neighbor]:

                    dfs(neighbor)

        complete = 0

        for i in range(n):

            if not visited[i]:

                component = []

                dfs(i)

                vertices = len(
                    component
                )

                edgeCount = 0

                for node in component:

                    edgeCount += len(
                        graph[node]
                    )

                edgeCount //= 2

                if (

                    edgeCount

                    ==

                    vertices
                    *
                    (vertices - 1)
                    //
                    2

                ):

                    complete += 1

        return complete


# ----------------------------------
# Pattern Used:
#
# Graph
#
# +
#
# DFS
#
# +
#
# Connected Components
#
#
# Why:
#
# Find every connected
# component.
#
# Count its vertices
# and edges.
#
# A component is complete
# only if every vertex
# is connected to every
# other vertex.
#
#
# My Thinking:
#
# 1. Build adjacency list.
#
# 2. Run DFS to find one
#    connected component.
#
# 3. Count vertices.
#
# 4. Count edges.
#
# 5. Compare with the
#    formula:
#
#       V*(V-1)/2
#
# 6. If equal,
#    component is complete.
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
# ----------------------------------


n = 6

edges = [

    [0,1],

    [0,2],

    [1,2],

    [3,4]

]

obj = Solution()

print(

    obj.countCompleteComponents(

        n,

        edges

    )

)

# Output:
# 3