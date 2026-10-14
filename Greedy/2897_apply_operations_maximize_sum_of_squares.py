
nums = [2, 6, 5, 8]
k = 2

MOD = 10**9 + 7
bit_count = [0] * 31

for num in nums:
    for bit in range(31):
        if num & (1 << bit):
            bit_count[bit] += 1

ans = 0

for _ in range(k):
    num = 0

    for bit in range(31):
        if bit_count[bit] > 0:
            num |= 1 << bit
            bit_count[bit] -= 1

    ans = (ans + num * num) % MOD

print(ans)  # Output: 261
