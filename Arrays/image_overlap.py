class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)

        ones1 = []
        ones2 = []

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))

                if img2[r][c] == 1:
                    ones2.append((r, c))

        shifts = {}

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                dr = r2 - r1
                dc = c2 - c1

                shifts[(dr, dc)] = shifts.get((dr, dc), 0) + 1

        return max(shifts.values(), default=0)


if __name__ == "__main__":
    solution = Solution()

    img1 = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

    img2 = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]

    print(solution.largestOverlap(img1, img2))