
from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1

        for i, num in enumerate(nums):
            if i != num:
                ans &= i & num

        return ans


if __name__ == "__main__":
    sol = Solution()

    print(sol.sortPermutation([0, 3, 2, 1]))  # 1
    print(sol.sortPermutation([0, 1, 3, 2]))  # 2
    print(sol.sortPermutation([3, 2, 1, 0]))  # 0
    print(sol.sortPermutation([0, 1, 2, 3]))  # 0
