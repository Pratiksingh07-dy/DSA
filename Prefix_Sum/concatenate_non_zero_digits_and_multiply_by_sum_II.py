class Solution:

    def sumAndMultiply(
        self,
        s,
        queries
    ):

        MOD = 10 ** 9 + 7

        n = len(s)

        digits = []
        positions = []

        for i, ch in enumerate(s):

            if ch != "0":

                digits.append(
                    int(ch)
                )

                positions.append(i)

        m = len(digits)

        if m == 0:

            return [
                0
            ] * len(queries)

        # Prefix sum of digits
        prefixSum = [
            0
        ] * (m + 1)

        for i in range(m):

            prefixSum[i + 1] = (
                prefixSum[i]
                + digits[i]
            )

        # Powers of 10
        power10 = [
            1
        ] * (m + 1)

        for i in range(1, m + 1):

            power10[i] = (
                power10[i - 1]
                * 10
            ) % MOD

        # Prefix concatenated number
        prefixNumber = [
            0
        ] * (m + 1)

        for i in range(m):

            prefixNumber[i + 1] = (
                prefixNumber[i]
                * 10
                + digits[i]
            ) % MOD

        # First non-zero index >= i
        first = [
            m
        ] * (n + 1)

        p = 0

        for i in range(n):

            while (
                p < m
                and positions[p] < i
            ):

                p += 1

            first[i] = p

        # Last non-zero index <= i
        last = [
            -1
        ] * n

        p = 0

        current = -1

        for i in range(n):

            while (
                p < m
                and positions[p] == i
            ):

                current = p

                p += 1

            last[i] = current

        answer = []

        for left, right in queries:

            L = first[left]

            R = last[right]

            if L > R:

                answer.append(0)

                continue

            length = R - L + 1

            x = (
                prefixNumber[R + 1]
                - prefixNumber[L]
                * power10[length]
            ) % MOD

            digitSum = (
                prefixSum[R + 1]
                - prefixSum[L]
            )

            answer.append(
                (x * digitSum) % MOD
            )

        return answer


# ----------------------------------
# Pattern Used:
#
# Prefix Sum
#
# +
#
# Prefix Preprocessing
#
# +
#
# Modular Arithmetic
#
#
# Why:
#
# Instead of processing
# every query from scratch,
# preprocess useful arrays.
#
# Each query then becomes
# O(1).
#
#
# My Thinking:
#
# 1. Store all non-zero
#    digits and positions.
#
# 2. Build prefix digit sums.
#
# 3. Build prefix numbers.
#
# 4. Build powers of 10.
#
# 5. Map each query to the
#    compressed digit array.
#
# 6. Compute answer using
#    prefix arrays.
#
#
# Time Complexity:
#
# O(n + q)
#
#
# Space Complexity:
#
# O(n)
# ----------------------------------


s = "10203004"

queries = [
    [0, 7],
    [1, 3],
    [4, 6]
]

obj = Solution()

print(
    obj.sumAndMultiply(
        s,
        queries
    )
)

# Output:
# [12340, 4, 9]