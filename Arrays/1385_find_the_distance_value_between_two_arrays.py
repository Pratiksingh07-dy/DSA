from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0

        for num in arr1:
            valid = True

            for other in arr2:
                if abs(num - other) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d = 2

    result = sol.findTheDistanceValue(arr1, arr2, d)
    print("Distance Value:", result)