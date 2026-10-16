
nums = [1, 2, 1]

n = len(nums)
ans = 0

for i in range(n):
    seen = set()

    for j in range(i, n):
        seen.add(nums[j])
        ans += len(seen) ** 2

print(ans)  # Output: 15
