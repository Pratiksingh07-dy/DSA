
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1
                tree_sq[node] = (
                    tree_sq[node] + 2 * tree_sum[node] + length
                ) % MOD
                tree_sum[node] = (tree_sum[node] + length) % MOD
                lazy[node] += 1
                return

            mid = (start + end) // 2
            lc = node * 2
            rc = lc + 1

            if lazy[node]:
                val = lazy[node]
                for child, lo, hi in (
                    (lc, start, mid),
                    (rc, mid + 1, end)
                ):
                    length = hi - lo + 1
                    tree_sq[child] = (
                        tree_sq[child]
                        + 2 * val * tree_sum[child]
                        + val * val * length
                    ) % MOD
                    tree_sum[child] = (
                        tree_sum[child] + val * length
                    ) % MOD
                    lazy[child] += val
                lazy[node] = 0

            if left <= mid:
                update(lc, start, mid, left, right)
            if right > mid:
                update(rc, mid + 1, end, left, right)

            tree_sum[node] = (
                tree_sum[lc] + tree_sum[rc]
            ) % MOD
            tree_sq[node] = (
                tree_sq[lc] + tree_sq[rc]
            ) % MOD

        ans = 0
        last_seen = {}

        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            ans = (ans + tree_sq[1]) % MOD
            last_seen[x] = i

        return ans
