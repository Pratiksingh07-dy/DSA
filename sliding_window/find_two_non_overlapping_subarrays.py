class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        best = [INF] * n
        left = 0
        current_sum = 0
        answer = INF
        min_length = INF

        for right in range(n):
            current_sum += arr[right]

            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, best[left - 1] + length)

                min_length = min(min_length, length)

            if right == 0:
                best[right] = min_length
            else:
                best[right] = min(best[right - 1], min_length)

        return -1 if answer == INF else answer


if __name__ == "__main__":
    solution = Solution()

    arr = [3, 2, 2, 4, 3]
    target = 3

    print(solution.minSumOfLengths(arr, target))