
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def check_increasing(arr):
            pos = arr.index(0)

            for i in range(n):
                if arr[(pos + i) % n] != i:
                    return -1

            return min(pos, (n - pos) % n + 2)

        def check_decreasing(arr):
            pos = arr.index(n - 1)

            for i in range(n):
                if arr[(pos + i) % n] != n - 1 - i:
                    return -1

            return min(pos + 1, (n - pos) % n + 1)

        ans = check_increasing(nums)

        reversed_nums = nums[::-1]
        rev_ans = check_increasing(reversed_nums)

        if rev_ans != -1:
            rev_ans = min(
                rev_ans + 1,
                (n - rev_ans) % n + 1
            )

        dec_ans = check_decreasing(nums)

        if dec_ans != -1:
            ans = dec_ans if ans == -1 else min(ans, dec_ans)

        if rev_ans != -1:
            ans = rev_ans if ans == -1 else min(ans, rev_ans)

        return ans


if __name__ == "__main__":
    sol = Solution()

    print(sol.minOperations([0, 2, 1]))     # Expected: 2
    print(sol.minOperations([1, 0, 2]))     # Expected: 2
    print(sol.minOperations([2, 0, 1, 3])) # Expected: -1
    print(sol.minOperations([1, 2, 3, 4, 0])) # Expected: 3
