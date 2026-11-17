class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Step 1: Precompute the cost of every substring
        cost = [[INF] * n for _ in range(n)]

        for left in range(n):
            for right in range(left + 1, n):
                length = right - left + 1

                # Try every valid divisor of the substring length
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Check each repeating-pattern group
                    for offset in range(d):
                        count = length // d

                        for t in range(count // 2):
                            i = left + offset + t * d
                            j = left + offset + (count - 1 - t) * d

                            if s[i] != s[j]:
                                changes += 1

                    cost[left][right] = min(
                        cost[left][right], changes
                    )

        # Step 2: DP for partitioning into exactly k substrings
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(parts * 2, n + 1):

                # j is the starting index of the last substring
                for j in range((parts - 1) * 2, i - 1):

                    if dp[parts - 1][j] == INF:
                        continue

                    dp[parts][i] = min(
                        dp[parts][i],
                        dp[parts - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]