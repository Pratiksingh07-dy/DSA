from collections import Counter


class Solution:

    def maximumLength(self, nums):

        freq = Counter(nums)

        answer = 1

        if 1 in freq:

            if freq[1] % 2 == 0:
                answer = max(answer, freq[1] - 1)
            else:
                answer = max(answer, freq[1])

        for x in list(freq.keys()):

            if x == 1:
                continue

            length = 0

            current = x

            while current in freq and freq[current] >= 2:

                length += 2

                if current * current > 10 ** 18:
                    break

                current *= current

            if current in freq:
                length += 1
            else:
                length -= 1

            answer = max(answer, length)

        return answer


# Test

nums = [5,4,1,2,2]

obj = Solution()

print(obj.maximumLength(nums))

# Output:
# 3


# -----------------------------
# Pattern Used:
# Hash Map (Frequency Counting)
#
# Why:
# Need to know how many
# times each number occurs.
#
# My thinking:
# 1. Count frequency.
# 2. Start from every
#    possible base x.
# 3. Keep squaring:
#    x -> x² -> x⁴...
# 4. Every middle element
#    needs two copies.
# 5. Last element needs
#    only one copy.
#
# Example:
#
# nums =
# [5,4,1,2,2]
#
# Possible chain:
#
# 2 -> 4
#
# Subset:
#
# [2,4,2]
#
# Length = 3
#
# Time Complexity:
# O(n log log M)
#
# Reason:
# Every chain grows by
# repeated squaring, so the
# number of squaring steps
# is very small.
#
# Space Complexity:
# O(n)
# -----------------------------