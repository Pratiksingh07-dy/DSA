from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for jump in range(1, 4):
                prev = i - jump

                if prev >= 0:
                    dp[i] = min(
                        dp[i],
                        dp[prev] + costs[i - 1] + jump * jump
                    )

        return dp[n]


if __name__ == "__main__":
    sol = Solution()

    n = 4
    costs = [1, 2, 3, 4]

    print(sol.climbStairs(n, costs))