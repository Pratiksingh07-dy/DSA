class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:

            width = right - left

            h = min(height[left], height[right])

            area = width * h

            maximum = max(maximum, area)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return maximum


obj = Solution()

print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
print(obj.maxArea([1,1]))