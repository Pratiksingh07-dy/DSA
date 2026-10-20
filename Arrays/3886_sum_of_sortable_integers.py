
def sumOfSortableIntegers(nums):
    n = len(nums)
    target = sorted(nums)
    ans = 0

    for k in range(1, n + 1):
        if n % k != 0:
            continue

        valid = True

        for start in range(0, n, k):
            chunk = nums[start:start + k]
            expected = target[start:start + k]
            doubled = chunk + chunk

            if not any(
                doubled[i:i + k] == expected
                for i in range(k)
            ):
                valid = False
                break

        if valid:
            ans += k

    return ans


print(sumOfSortableIntegers([3, 1, 2]))  # Output: 3
print(sumOfSortableIntegers([7, 6, 5]))  # Output: 0
print(sumOfSortableIntegers([5, 8]))     # Output: 3
