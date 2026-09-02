def uniformArray(nums1):
    has_odd = False
    has_even = False

    for num in nums1:
        if num % 2 == 0:
            has_even = True
        else:
            has_odd = True

    if not has_odd or not has_even:
        return True

    return len(nums1) > 1


nums1 = list(map(int, input().split()))

print(uniformArray(nums1))