
nums = [1, 2, 5, 2, 3]
target = 2

nums.sort()
result = []

for i in range(len(nums)):
    if nums[i] == target:
        result.append(i)

print(result)  # Output: [1, 2]
