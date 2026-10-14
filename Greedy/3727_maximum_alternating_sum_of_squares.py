
nums = [1, 2, 3]

squares = sorted(x * x for x in nums)
n = len(squares)

answer = sum(squares[n // 2:]) - sum(squares[:n // 2])

print(answer)  # Output: 12
