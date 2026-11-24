from typing import List
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        for i in range(n):
            product = 1
            current_gcd = 0
            current_lcm = 1

            for j in range(i, n):
                num = nums[j]

                product *= num
                current_gcd = gcd(current_gcd, num)
                current_lcm = lcm(current_lcm, num)

                if product == current_gcd * current_lcm:
                    answer = max(answer, j - i + 1)

        return answer