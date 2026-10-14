
num = 2
digit_sum = 17

if digit_sum > 9 * num:
    answer = ""
else:
    digits = []

    for _ in range(num):
        digit = min(9, digit_sum)
        digits.append(str(digit))
        digit_sum -= digit

    answer = "".join(digits) if digit_sum == 0 else ""

print(answer)  # Output: 98
