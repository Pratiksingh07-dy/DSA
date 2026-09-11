class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        numbers = set()

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if j == i:
                    continue

                for k in range(len(digits)):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    numbers.add(number)

        return len(numbers)


if __name__ == "__main__":
    solution = Solution()

    digits = [1, 2, 3, 4]

    print(solution.totalNumbers(digits))