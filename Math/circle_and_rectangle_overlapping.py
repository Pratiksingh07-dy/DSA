class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                      x1: int, y1: int, x2: int, y2: int) -> bool:

        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        dx = closestX - xCenter
        dy = closestY - yCenter

        return dx * dx + dy * dy <= radius * radius


if __name__ == "__main__":
    solution = Solution()

    radius = 1
    xCenter = 0
    yCenter = 0
    x1 = 1
    y1 = -1
    x2 = 3
    y2 = 1

    print(solution.checkOverlap(
        radius, xCenter, yCenter,
        x1, y1, x2, y2
    ))