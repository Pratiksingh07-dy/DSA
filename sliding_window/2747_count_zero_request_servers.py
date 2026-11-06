from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        freq = defaultdict(int)
        ans = [0] * len(queries)

        left = 0
        right = 0
        active = 0

        for q, idx in sorted_queries:
            # Add requests occurring at or before q.
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if freq[server] == 0:
                    active += 1

                freq[server] += 1
                right += 1

            # Remove requests older than q - x.
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans