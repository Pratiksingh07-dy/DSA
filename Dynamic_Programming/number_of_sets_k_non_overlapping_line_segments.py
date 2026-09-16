class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [1] * n

        for _ in range(k):
            new_dp = [0] * n
            extend = 0

            for i in range(1, n):
                extend = (extend + dp[i - 1]) % MOD
                new_dp[i] = (new_dp[i - 1] + extend) % MOD

            dp = new_dp

        return dp[n - 1]


if __name__ == "__main__":
    n = 4
    k = 2

    solution = Solution()
    print(solution.numberOfSets(n, k))