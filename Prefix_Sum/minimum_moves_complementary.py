
#1674. Minimum Moves to Make Array Complementary

class Solution:
    def minMoves(self, nums, limit):

        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b)
            high = max(a, b)

            diff[2] += 2

            diff[low + 1] -= 1

            diff[a + b] -= 1

            diff[a + b + 1] += 1

            diff[high + limit + 1] += 1

        moves = float('inf')

        current = 0

        for s in range(2, 2 * limit + 1):

            current += diff[s]

            moves = min(moves, current)

        return moves


# Test Code
nums=[1,2,4,3]
limit=4

obj=Solution()

answer=obj.minMoves(nums,limit)

print(answer)


# -----------------------------
# Pattern Used: Difference Array
#
# Why:
# Need fast range updates instead
# of checking every sum separately
#
# My thinking:
# 1. Form pairs from both ends
# 2. Find move cost ranges
# 3. Mark changes using diff array
# 4. Build prefix sum
# 5. Find minimum moves
#
# Time Complexity: O(n+limit)
# Space Complexity: O(limit)
# -----------------------------