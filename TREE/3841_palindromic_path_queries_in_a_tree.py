
from typing import List


class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        # Build parent, depth and traversal order.
        order = [0]
        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        # Find the largest child subtree for each node.
        for u in reversed(order):
            largest = 0
            for v in graph[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        current = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = current
                current += 1

                for v in graph[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # XOR segment tree over HLD positions.
        seg = [0] * (2 * n)

        for u, ch in enumerate(s):
            seg[n + pos[u]] = 1 << (ord(ch) - ord('a'))

        for i in range(n - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(index, value):
            i = n + index
            seg[i] = value
            i //= 2

            while i:
                seg[i] = seg[2 * i] ^ seg[2 * i + 1]
                i //= 2

        def range_xor(left, right):
            result = 0
            left += n
            right += n + 1

            while left < right:
                if left & 1:
                    result ^= seg[left]
                    left += 1
                if right & 1:
                    right -= 1
                    result ^= seg[right]

                left //= 2
                right //= 2

            return result

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])
            return result

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                ch = parts[2]
                update(pos[u], 1 << (ord(ch) - ord('a')))
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = path_xor(u, v)

                # A palindrome permutation allows at most one odd count.
                answer.append((mask & (mask - 1)) == 0)

        return answer
