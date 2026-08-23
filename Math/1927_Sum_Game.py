def sumGame(num):
    n = len(num)
    mid = n // 2

    left_sum = 0
    right_sum = 0
    left_q = 0
    right_q = 0

    for i in range(mid):
        if num[i] == '?':
            left_q += 1
        else:
            left_sum += int(num[i])

    for i in range(mid, n):
        if num[i] == '?':
            right_q += 1
        else:
            right_sum += int(num[i])

    diff = left_sum - right_sum
    q_diff = right_q - left_q

    if 2 * diff == 9 * q_diff:
        return False

    return True


num = "?6?6?000?3"

print(sumGame(num))