from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        odd = 0
        even = 1
        prefix_sum = 0
        answer = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                answer += odd
                even += 1
            else:
                answer += even
                odd += 1

        return answer % MOD