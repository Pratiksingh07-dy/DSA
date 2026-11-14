from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minimum = float('inf')

        for start in range(n):
            current_sum = 0

            for end in range(start, min(n, start + r)):
                current_sum += nums[end]
                length = end - start + 1

                if l <= length <= r and current_sum > 0:
                    minimum = min(minimum, current_sum)

        return minimum if minimum != float('inf') else -1