from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, value):
        while i <= self.n:
            self.tree[i] += value
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def kth(self, k):
        idx = 0
        bit = 1 << (self.n.bit_length() - 1)

        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                idx = nxt
                k -= self.tree[nxt]
            bit >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        values = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(values)}
        size = len(values)

        counts = Fenwick(size)
        sums = Fenwick(size)

        def update(value, delta):
            idx = rank[value]
            counts.add(idx, delta)
            sums.add(idx, value * delta)

        def window_cost():
            median_idx = counts.kth((x + 1) // 2)
            median = values[median_idx - 1]

            left_count = counts.query(median_idx)
            left_sum = sums.query(median_idx)

            total_sum = sums.query(size)
            right_count = x - left_count
            right_sum = total_sum - left_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        costs = []

        for i in range(n):
            update(nums[i], 1)

            if i >= x:
                update(nums[i - x], -1)

            if i >= x - 1:
                costs.append(window_cost())

        # dp[j][i] = minimum cost to choose j non-overlapping
        # subarrays from the first i elements.
        INF = float("inf")
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(j * x, n + 1):
                # Option 1: Do not choose a subarray ending at i - 1.
                curr[i] = curr[i - 1]

                # Option 2: Choose the last x elements as a subarray.
                start = i - x
                curr[i] = min(
                    curr[i],
                    prev[start] + costs[start]
                )

            prev = curr

        return prev[n]