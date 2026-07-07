def sumAndMultiply(n):

    digits = []

    while n > 0:

        digit = n % 10

        if digit != 0:

            digits.append(str(digit))

        n //= 10

    if not digits:

        return 0

    digits.reverse()

    x = int("".join(digits))

    digitSum = sum(int(d) for d in digits)

    return x * digitSum


n = int(input())

print(sumAndMultiply(n))