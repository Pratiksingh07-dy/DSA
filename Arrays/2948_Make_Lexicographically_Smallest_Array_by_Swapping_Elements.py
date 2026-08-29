def lexicographicallySmallestArray(nums, limit):

    arr = sorted((x, i) for i, x in enumerate(nums))

    ans = nums[:]
    n = len(nums)

    i = 0

    while i < n:
        j = i

        while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
            j += 1

        values = [arr[k][0] for k in range(i, j + 1)]
        indices = sorted(arr[k][1] for k in range(i, j + 1))

        for k in range(len(values)):
            ans[indices[k]] = values[k]

        i = j + 1

    return ans


nums = list(map(int, input().split()))
limit = int(input())

print(lexicographicallySmallestArray(nums, limit))