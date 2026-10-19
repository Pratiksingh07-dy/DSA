
def numOfWays(nums):
    MOD = 10**9 + 7
    n = len(nums)

    comb = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        comb[i][0] = comb[i][i] = 1
        for j in range(1, i):
            comb[i][j] = (
                comb[i - 1][j - 1] + comb[i - 1][j]
            ) % MOD

    def dfs(arr):
        if len(arr) <= 2:
            return 1

        root = arr[0]
        left = [x for x in arr[1:] if x < root]
        right = [x for x in arr[1:] if x > root]

        return (
            comb[len(arr) - 1][len(left)]
            * dfs(left)
            * dfs(right)
        ) % MOD

    return (dfs(nums) - 1) % MOD


print(numOfWays([2, 1, 3]))  # Output: 1
print(numOfWays([3, 4, 5, 1, 2]))  # Output: 5
print(numOfWays([1, 2, 3]))  # Output: 0
