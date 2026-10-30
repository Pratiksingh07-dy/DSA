
from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]],
                     labels: str, k: int) -> int:

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # State: (cost, node, consecutive_count)
        pq = [(0, 0, 1)]
        dist = {}

        while pq:
            cost, node, count = heapq.heappop(pq)

            state = (node, count)

            if state in dist:
                continue

            dist[state] = cost

            if node == n - 1:
                return cost

            for nxt, weight in graph[node]:
                if labels[nxt] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count <= k:
                    new_state = (nxt, new_count)

                    if new_state not in dist:
                        heapq.heappush(
                            pq,
                            (cost + weight, nxt, new_count)
                        )

        return -1
