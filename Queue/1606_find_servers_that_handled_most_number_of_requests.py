from typing import List
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        size = 1
        while size < k:
            size *= 2

        # Segment tree: 1 means available, 0 means busy.
        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(server, available):
            pos = size + server
            tree[pos] = available

            pos //= 2
            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find_first(left, right):
            # Find the first available server in [left, right).
            def search(node, start, end):
                if end <= left or start >= right or tree[node] == 0:
                    return -1

                if end - start == 1:
                    return start

                mid = (start + end) // 2

                result = search(node * 2, start, mid)

                if result != -1:
                    return result

                return search(node * 2 + 1, mid, end)

            return search(1, 0, size)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            current_time = arrival[i]

            # Release servers whose tasks have finished.
            while busy and busy[0][0] <= current_time:
                finish_time, server = heapq.heappop(busy)
                update(server, 1)

            start = i % k

            # Find the next available server, with wraparound.
            server = find_first(start, k)

            if server == -1:
                server = find_first(0, start)

            # Drop the request if all servers are busy.
            if server == -1:
                continue

            count[server] += 1

            update(server, 0)

            finish_time = current_time + load[i]
            heapq.heappush(busy, (finish_time, server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]