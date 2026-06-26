class Fenwick:

    def __init__(self, n):

        self.bit = [0] * (n + 2)

    def update(self, index, value):

        while index < len(self.bit):

            self.bit[index] += value

            index += index & -index

    def query(self, index):

        total = 0

        while index > 0:

            total += self.bit[index]

            index -= index & -index

        return total


class Solution:

    def countMajoritySubarrays(self, nums, target):

        n = len(nums)

        offset = n + 2

        bit = Fenwick(2 * n + 5)

        prefix = 0

        answer = 0

        bit.update(offset, 1)

        for num in nums:

            if num == target:
                prefix += 1
            else:
                prefix -= 1

            answer += bit.query(prefix + offset - 1)

            bit.update(prefix + offset, 1)

        return answer


# Test

nums = [1,2,2,3]
target = 2

obj = Solution()

print(
    obj.countMajoritySubarrays(
        nums,
        target
    )
)

# Output:
# 5


# -----------------------------
# Pattern Used:
# Prefix Sum + Fenwick Tree
#
# Why:
# Convert the problem into
# counting subarrays whose
# prefix-sum difference is
# positive.
#
# My thinking:
# 1. Replace target by +1.
# 2. Replace every other
#    number by -1.
# 3. Majority means the
#    transformed subarray
#    sum > 0.
# 4. Use prefix sums.
# 5. Count previous prefix
#    sums smaller than the
#    current prefix using
#    a Fenwick Tree.
#
# Time Complexity:
# O(n log n)
#
# Space Complexity:
# O(n)
# -----------------------------